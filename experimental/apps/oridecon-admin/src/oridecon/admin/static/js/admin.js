/**
 * Oridecon Admin - Core JavaScript
 */
(function() {
  'use strict';

  // Initialize admin when DOM is ready
  document.addEventListener('DOMContentLoaded', function() {
    initSidebar();
    initToasts();
    initModals();
    initForms();
    initKeyboardShortcuts();
  });

  // ========== Bulk export download (B28) ==========
  // Export buttons render onclick="return window.LexigramDownloadBulk(this)"
  // with data-bulk-download-url / data-bulk-action attributes. CSV/JSON
  // responses carry Content-Disposition and must bypass HTMX (whose swap
  // would inject the file into the page), so we fetch and download a blob.
  window.LexigramDownloadBulk = function(btn) {
    downloadBulk(btn);
    return false;
  };

  async function downloadBulk(btn) {
    function toast(message, type) {
      if (window.showToast) window.showToast(message, type);
    }
    function serializeTableQuery(table) {
      const params = new URLSearchParams();
      const ignored = new Set(['ids', 'csrf_token', 'action', 'scope', 'list_query']);
      table.querySelectorAll('input[name], select[name], textarea[name]').forEach(function(control) {
        if (control.disabled || ignored.has(control.name)) return;
        const type = String(control.type || '').toLowerCase();
        if ((type === 'checkbox' || type === 'radio') && !control.checked) return;
        if (control.tagName === 'SELECT' && control.multiple) {
          Array.from(control.selectedOptions).forEach(function(option) {
            params.append(control.name, option.value);
          });
        } else if (!['button', 'file', 'reset', 'submit'].includes(type)) {
          params.append(control.name, control.value);
        }
      });
      return params.toString();
    }
    try {
      const url = btn.getAttribute('data-bulk-download-url');
      if (!url) return;
      const action = btn.getAttribute('data-bulk-action') || 'export';
      const table = btn.closest('[data-oridecon-table-root]');
      if (!table) return;
      const checked = table.querySelectorAll('input[name="ids"]:checked');
      const filtered = !checked.length;
      const body = new FormData();
      body.append('action', action);
      if (filtered) {
        // R25: no selection means "export everything matching this table's
        // current view" — sibling tables may hold independent state.
        body.append('scope', 'filtered');
        body.append('list_query', serializeTableQuery(table));
      } else {
        checked.forEach(function(box) { body.append('ids', box.value); });
      }
      const csrfInput = table.querySelector('input[name="csrf_token"]');
      const csrfEl = document.querySelector('[data-csrf-token]');
      const csrf = (csrfInput && csrfInput.value) ||
        window.__orideconCsrfToken ||
        (csrfEl && csrfEl.getAttribute('data-csrf-token'));
      if (csrf) body.append('csrf_token', csrf);
      const headers = {};
      if (csrf) headers['X-CSRF-Token'] = csrf;

      const response = await fetch(url, {
        method: 'POST',
        body: body,
        headers: headers,
        credentials: 'same-origin'
      });
      if (!response.ok) {
        toast('Export failed (' + response.status + ').', 'error');
        return;
      }
      const blob = await response.blob();
      const disposition = response.headers.get('Content-Disposition') || '';
      const match = disposition.match(/filename="?([^";]+)"?/i);
      const filename = match ? match[1] : 'export.csv';
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = filename;
      document.body.appendChild(link);
      link.click();
      link.remove();
      setTimeout(function() { URL.revokeObjectURL(link.href); }, 4000);
      toast(
        filtered
          ? 'Exported all records matching the current view.'
          : 'Exported ' + checked.length + ' record' + (checked.length === 1 ? '' : 's') + '.',
        'success'
      );
    } catch (err) {
      toast('Export failed.', 'error');
    }
  }

  // ========== Sidebar ==========
  function initSidebar() {
    const sidebar = document.querySelector('.admin-sidebar');
    const toggle = document.querySelector('[data-toggle="sidebar"]');
    const menuItems = document.querySelectorAll('.sidebar-menu-item');
    
    if (toggle && sidebar) {
      toggle.addEventListener('click', function() {
        document.body.classList.toggle('sidebar-collapsed');
        localStorage.setItem('sidebarCollapsed', 
          document.body.classList.contains('sidebar-collapsed'));
      });
    }
    
    // Restore sidebar state
    if (localStorage.getItem('sidebarCollapsed') === 'true') {
      document.body.classList.add('sidebar-collapsed');
    }
    
    // Submenu toggles
    menuItems.forEach(function(item) {
      const submenu = item.querySelector('.sidebar-submenu');
      if (submenu) {
        const link = item.querySelector('.sidebar-link');
        link.addEventListener('click', function(e) {
          if (submenu) {
            e.preventDefault();
            item.classList.toggle('open');
          }
        });
      }
    });
  }

  // ========== Toast Notifications ==========
  function initToasts() {
    window.showToast = function(message, type, duration) {
      type = type || 'info';
      duration = duration || 3000;
      
      // The server-rendered flash zone is #flash-container; client-created
      // toasts use .toast-container. Reuse either global overlay so a flash
      // response never leaves a second container in document flow.
      const container =
        document.querySelector('.toast-container, #flash-container') ||
        createToastContainer();
      const toast = document.createElement('div');
      toast.className = 'toast toast-' + type;
      toast.innerHTML = '<span class="toast-message">' + escapeHtml(message) + '</span>' +
                       '<button class="toast-close" aria-label="Close">&times;</button>';
      
      container.appendChild(toast);
      
      // Animate in
      requestAnimationFrame(function() {
        toast.classList.add('show');
      });
      
      // Auto remove
      const timeout = setTimeout(function() {
        removeToast(toast);
      }, duration);
      
      // Close button
      toast.querySelector('.toast-close').addEventListener('click', function() {
        clearTimeout(timeout);
        removeToast(toast);
      });
    };
    
    function createToastContainer() {
      const container = document.createElement('div');
      container.className = 'toast-container';
      document.body.appendChild(container);
      return container;
    }
    
    function removeToast(toast) {
      toast.classList.remove('show');
      toast.addEventListener('transitionend', function() {
        toast.remove();
      });
    }

    // CSP-clean replacements for the inline toast handlers
    // (data-action / data-dismiss-toast descriptors instead of onclick).
    window.dismissToast = function(id) {
      const toast = document.getElementById(id);
      if (toast) toast.remove();
    };
    document.addEventListener('submit', function(event) {
      const form = event.target;
      const message = form && form.getAttribute
        ? form.getAttribute('data-confirm') : null;
      if (!message) return;
      if (window.confirm(message)) return;
      event.preventDefault();
      event.stopImmediatePropagation();
    }, true);
    document.addEventListener('click', function(event) {
      if (event.defaultPrevented || event.button !== 0) return;
      const el = event.target instanceof Element
        ? event.target.closest('[data-action]') : null;
      if (!el) return;
      const action = el.getAttribute('data-action');
      if (action === 'dismiss-toast') {
        const id = el.getAttribute('data-dismiss-toast');
        if (id && window.dismissToast) window.dismissToast(id);
        else {
          const toast = el.closest('[role="alert"]') || el.parentElement;
          if (toast) toast.remove();
        }
        event.preventDefault();
      } else if (action === 'dismiss-alert') {
        const container = el.closest('[role="alert"]') || el.parentElement;
        if (container) container.remove();
        event.preventDefault();
      } else if (action === 'reload') {
        window.location.reload();
        event.preventDefault();
      }
    }, true);
  }

  // ========== Modals ==========
  function initModals() {
    document.addEventListener('click', function(e) {
      // Open modal
      const trigger = e.target.closest('[data-modal]');
      if (trigger) {
        e.preventDefault();
        const modalId = trigger.getAttribute('data-modal');
        const modal = document.getElementById(modalId);
        if (modal) openModal(modal);
      }
      
      // Close modal
      if (e.target.matches('.modal-backdrop, [data-dismiss="modal"]')) {
        const modal = e.target.closest('.modal');
        if (modal) closeModal(modal);
      }
    });
    
    // ESC to close
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        const openModal = document.querySelector('.modal.show');
        if (openModal) closeModal(openModal);
      }
    });
    
    window.openModal = function(modal) {
      if (typeof modal === 'string') {
        modal = document.getElementById(modal);
      }
      if (!modal) return;
      
      modal.classList.add('show');
      document.body.classList.add('modal-open');
      modal.setAttribute('aria-hidden', 'false');
      
      const focusable = modal.querySelector('input, button, [tabindex]:not([tabindex="-1"])');
      if (focusable) focusable.focus();
    };
    
    window.closeModal = function(modal) {
      if (typeof modal === 'string') {
        modal = document.getElementById(modal);
      }
      if (!modal) return;
      
      modal.classList.remove('show');
      document.body.classList.remove('modal-open');
      modal.setAttribute('aria-hidden', 'true');
    };
  }

  // ========== Forms ==========
  function initForms() {
    // Saved views (R13): the "save current view" form is rendered outside
    // the HTMX swap zones, so its server-rendered `query` value goes stale
    // after client-side filtering. Sync it with the live URL at submit time
    // (delegated — survives any DOM swaps; the server re-sanitizes anyway).
    document.addEventListener('submit', function(e) {
      const form = e.target.closest ? e.target.closest('form[data-saved-view-save]') : null;
      if (!form) return;
      const queryInput = form.querySelector('input[name="query"]');
      if (queryInput) {
        queryInput.value = window.location.search.replace(/^\?/, '');
      }
    });

    // Form validation feedback
    document.querySelectorAll('form[data-validate]').forEach(function(form) {
      form.addEventListener('submit', function(e) {
        if (!form.checkValidity()) {
          e.preventDefault();
          e.stopPropagation();
        }
        form.classList.add('was-validated');
      });
    });
    
    // Confirm dialogs
    document.addEventListener('click', function(e) {
      const trigger = e.target.closest('[data-confirm]');
      if (trigger) {
        const message = trigger.getAttribute('data-confirm');
        if (!confirm(message)) {
          e.preventDefault();
        }
      }
    });
    
    // AJAX form submissions
    document.querySelectorAll('form[data-ajax]').forEach(function(form) {
      form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const submitBtn = form.querySelector('[type="submit"]');
        const originalText = submitBtn ? submitBtn.textContent : '';
        
        try {
          if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.textContent = 'Saving...';
          }
          
          const formData = new FormData(form);
          const response = await fetch(form.action, {
            method: form.method || 'POST',
            body: formData,
            headers: {
              'X-Requested-With': 'XMLHttpRequest'
            }
          });
          
          if (response.ok) {
            const data = await response.json();
            if (data.redirect) {
              window.location.href = data.redirect;
            } else if (data.message) {
              showToast(data.message, 'success');
            }
          } else {
            const error = await response.json();
            showToast(error.message || 'An error occurred', 'error');
          }
        } catch (err) {
          showToast('Network error', 'error');
        } finally {
          if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.textContent = originalText;
          }
        }
      });
    });
  }

  // ========== Keyboard Shortcuts ==========
  function initKeyboardShortcuts() {
    document.addEventListener('keydown', function(e) {
      // Cmd/Ctrl + K for command palette
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        const palette = document.getElementById('command-palette');
        if (palette) {
          toggleCommandPalette();
        }
      }
      
      // Cmd/Ctrl + S to save current form
      if ((e.metaKey || e.ctrlKey) && e.key === 's') {
        const activeForm = document.querySelector('form:not([data-no-shortcut])');
        if (activeForm && document.activeElement.closest('form') === activeForm) {
          e.preventDefault();
          activeForm.requestSubmit();
        }
      }
    });
  }

  // ========== Command Palette ==========
  window.toggleCommandPalette = function() {
    const palette = document.getElementById('command-palette');
    if (!palette) return;
    
    if (palette.classList.contains('show')) {
      palette.classList.remove('show');
    } else {
      palette.classList.add('show');
      const input = palette.querySelector('input');
      if (input) {
        input.value = '';
        input.focus();
      }
    }
  };

  // ========== Utilities ==========
  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Expose utilities
  window.LexigramAdmin = {
    showToast: function(msg, type, dur) { return window.showToast(msg, type, dur); },
    openModal: function(m) { return window.openModal(m); },
    closeModal: function(m) { return window.closeModal(m); },
    toggleCommandPalette: toggleCommandPalette
  };

  // ========== Delegated actions (CSP: no inline onclick/onsubmit) ==========
  // Legacy layouts (admin_layout.py) render components with data-action /
  // data-confirm descriptors; a capture-phase listener owns the behaviour so
  // no inline event-handler attribute is emitted.
  window.toggleTheme = function() {
    var dark = !document.documentElement.classList.contains('dark');
    document.documentElement.classList.toggle('dark', dark);
    localStorage.setItem('darkMode', String(dark));
    window.dispatchEvent(new CustomEvent('darkmode-change', { detail: { dark: dark } }));
  };
  window.toggleSidebar = function() {
    document.body.classList.toggle('sidebar-open');
  };
  window.closeSidebar = function() {
    document.body.classList.remove('sidebar-open');
  };
  window.openSidebar = function() {
    document.body.classList.add('sidebar-open');
  };

  document.addEventListener('submit', function (event) {
    var form = event.target;
    var message = form && form.getAttribute ? form.getAttribute('data-confirm') : null;
    if (!message) return;
    if (window.confirm(message)) return;
    event.preventDefault();
    event.stopImmediatePropagation();
  }, true);

  document.addEventListener('click', function (event) {
    if (event.defaultPrevented || event.button !== 0) return;
    var el = event.target instanceof Element ? event.target.closest('[data-action]') : null;
    if (!el) return;
    var action = el.getAttribute('data-action');
    var handled = true;
    switch (action) {
      case 'reload':
        window.location.reload();
        break;
      case 'dismiss-alert':
        var container = el.closest('[role="alert"]') || el.parentElement;
        if (container) container.remove();
        break;
      case 'dismiss-fragment':
        var fragment = el.closest('.admin-error-fragment');
        if (fragment) fragment.remove();
        break;
      case 'toggle-hidden':
        var targetId = el.getAttribute('data-toggle-target');
        var target = targetId ? document.getElementById(targetId) : null;
        if (target) target.classList.toggle('hidden');
        break;
      case 'dismiss-toast': {
        var toastId = el.getAttribute('data-dismiss-toast') || el.getAttribute('data-action-target');
        if (toastId && window.dismissToast) window.dismissToast(toastId);
        else {
          var toast = el.closest('[role="alert"]') || el.parentElement;
          if (toast) toast.remove();
        }
        break;
      }
      case 'dismiss-modal': {
        var modalId = el.getAttribute('data-dismiss-modal');
        var modal = modalId ? document.getElementById(modalId) : null;
        if (modal) modal.classList.add('hidden');
        break;
      }
      case 'bulk-download':
        if (window.LexigramDownloadBulk) window.LexigramDownloadBulk(el);
        break;
      case 'prevent':
        handled = false;
        event.preventDefault();
        break;
      case 'open-sidebar':
        window.openSidebar();
        break;
      case 'close-sidebar':
        window.closeSidebar();
        break;
      case 'toggle-sidebar':
        window.toggleSidebar();
        break;
      case 'toggle-sidebar-item':
        if (el.parentElement) el.parentElement.classList.toggle('is-collapsed');
        break;
      case 'toggle-sidebar-group':
        if (el.parentElement) el.parentElement.classList.toggle('is-expanded');
        break;
      case 'toggle-theme':
        if (window.toggleTheme) window.toggleTheme();
        break;
      default:
        handled = false;
    }
    if (handled) event.preventDefault();
  }, true);

})();
