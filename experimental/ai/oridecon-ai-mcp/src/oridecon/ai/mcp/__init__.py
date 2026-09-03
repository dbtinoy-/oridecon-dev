"""oridecon-mcp — MCP Server for Oridecon Framework.

Canonical import paths
-----------------------
MCPServer:         from oridecon.ai.mcp import MCPServer
MCPClient:         from oridecon.ai.mcp import MCPClient
MCPConfig:        from oridecon.ai.mcp import MCPConfig
ToolHandler:      from oridecon.ai.mcp import ToolHandler
ResourceHandler:  from oridecon.ai.mcp import ResourceHandler
PromptHandler:    from oridecon.ai.mcp import PromptHandler
StdioTransport:   from oridecon.ai.mcp import StdioTransport
SSETransport:     from oridecon.ai.mcp import SSETransport
MCPModule:        from oridecon.ai.mcp import MCPModule
MCPProvider:       from oridecon.ai.mcp import MCPProvider

Quick Start
-----------

    from oridecon.ai.mcp import MCPServer, MCPModule
    from oridecon import OrideconApplication

    app = OrideconApplication(
        modules=[..., MCPModule()],
    )

    await app.run()
"""

from __future__ import annotations

import importlib.metadata
import pkgutil
from typing import TYPE_CHECKING, Any

__path__ = pkgutil.extend_path(__path__, __name__)

from oridecon.ai.mcp.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.ai.mcp import MCPModule  # type: ignore[attr-defined]
    from oridecon.ai.mcp.adapters import ToolRegistryAdapter
    from oridecon.ai.mcp.client.core import (
        MCPClient,
        MCPClientTransport,
        SSEClientTransport,
        StdioClientTransport,
    )
    from oridecon.ai.mcp.client.module import (
        MCPClientModule,
        MCPClientProvider,
        MCPClientRegistry,
        MCPConnection,
    )
    from oridecon.ai.mcp.config import MCPConfig
    from oridecon.ai.mcp.controllers import (
        ControllerPromptProvider,
        ControllerResourceProvider,
        ControllerToolProvider,
        MCPController,
        ModulePromptProvider,
        ModuleResourceProvider,
        ModuleToolProvider,
        ServiceToolProvider,
    )
    from oridecon.ai.mcp.decorators import (
        prompt,
        resource,
        tool,
    )
    from oridecon.ai.mcp.di.provider import MCPProvider
    from oridecon.ai.mcp.exceptions import (
        MCPError,
        MCPInitializationError,
        MCPMethodNotFoundError,
        MCPPromptError,
        MCPProtocolError,
        MCPResourceError,
        MCPToolCallError,
        MCPTransportError,
    )
    from oridecon.ai.mcp.hooks import (
        MCPServerStartedHook,
        MCPServerStoppedHook,
        MCPToolInvokedHook,
    )
    from oridecon.ai.mcp.protocols import (
        MCPPromptHandlerProtocol,
        MCPPromptProviderProtocol,
        MCPResourceHandlerProtocol,
        MCPResourceProviderProtocol,
        MCPServerProtocol,
        MCPToolHandlerProtocol,
        MCPToolProviderProtocol,
        MCPTransportProtocol,
    )
    from oridecon.ai.mcp.server import MCPServer
    from oridecon.ai.mcp.server.handlers import (
        PromptHandler,
        ResourceHandler,
        ToolHandler,
    )
    from oridecon.ai.mcp.transport import (
        AbstractTransport,
        SSETransport,
        StdioTransport,
    )
    from oridecon.ai.mcp.types import (
        MCPInitializeResult,
        MCPJSONRPCRequest,
        MCPJSONRPCResponse,
        MCPPrompt,
        MCPPromptMessage,
        MCPResource,
        MCPResourceContent,
        MCPServerCapabilities,
        MCPServerInfo,
        MCPToolDefinition,
        MCPToolResult,
    )

_LAZY_IMPORTS: dict[str, str] = {
    "AbstractTransport": "oridecon.ai.mcp.transport",
    "ControllerPromptProvider": "oridecon.ai.mcp.controllers",
    "ControllerResourceProvider": "oridecon.ai.mcp.controllers",
    "ControllerToolProvider": "oridecon.ai.mcp.controllers",
    # Hooks
    "MCPServerStartedHook": "oridecon.ai.mcp.hooks",
    "MCPServerStoppedHook": "oridecon.ai.mcp.hooks",
    "MCPToolInvokedHook": "oridecon.ai.mcp.hooks",
    "MCPController": "oridecon.ai.mcp.controllers",
    "MCPInitializeResult": "oridecon.ai.mcp.types",
    "MCPJSONRPCRequest": "oridecon.ai.mcp.types",
    "MCPJSONRPCResponse": "oridecon.ai.mcp.types",
    "MCPPrompt": "oridecon.ai.mcp.types",
    "MCPPromptMessage": "oridecon.ai.mcp.types",
    "MCPResource": "oridecon.ai.mcp.types",
    "MCPResourceContent": "oridecon.ai.mcp.types",
    "MCPServerCapabilities": "oridecon.ai.mcp.types",
    "MCPServerInfo": "oridecon.ai.mcp.types",
    "MCPToolDefinition": "oridecon.ai.mcp.types",
    "MCPToolResult": "oridecon.ai.mcp.types",
    "ModulePromptProvider": "oridecon.ai.mcp.controllers",
    "ModuleResourceProvider": "oridecon.ai.mcp.controllers",
    "ModuleToolProvider": "oridecon.ai.mcp.controllers",
    "ServiceToolProvider": "oridecon.ai.mcp.controllers",
    "MCPClient": "oridecon.ai.mcp.client.core",
    "MCPClientModule": "oridecon.ai.mcp.client.module",
    "MCPClientProvider": "oridecon.ai.mcp.client.module",
    "MCPClientRegistry": "oridecon.ai.mcp.client.module",
    "MCPConnection": "oridecon.ai.mcp.client.module",
    "MCPClientTransport": "oridecon.ai.mcp.client.core",
    "MCPConfig": "oridecon.ai.mcp.config",
    "MCPError": "oridecon.ai.mcp.exceptions",
    "MCPInitializationError": "oridecon.ai.mcp.exceptions",
    "MCPMethodNotFoundError": "oridecon.ai.mcp.exceptions",
    "MCPModule": "oridecon.ai.mcp.module",
    "MCPPromptError": "oridecon.ai.mcp.exceptions",
    "MCPProtocolError": "oridecon.ai.mcp.exceptions",
    "MCPProvider": "oridecon.ai.mcp.di.provider",
    "MCPResourceError": "oridecon.ai.mcp.exceptions",
    "MCPServer": "oridecon.ai.mcp.server",
    "MCPToolCallError": "oridecon.ai.mcp.exceptions",
    "MCPTransportError": "oridecon.ai.mcp.exceptions",
    # Protocols
    "MCPToolProviderProtocol": "oridecon.ai.mcp.protocols",
    "MCPResourceProviderProtocol": "oridecon.ai.mcp.protocols",
    "MCPPromptProviderProtocol": "oridecon.ai.mcp.protocols",
    "MCPTransportProtocol": "oridecon.ai.mcp.protocols",
    "MCPServerProtocol": "oridecon.ai.mcp.protocols",
    "MCPToolHandlerProtocol": "oridecon.ai.mcp.protocols",
    "MCPResourceHandlerProtocol": "oridecon.ai.mcp.protocols",
    "MCPPromptHandlerProtocol": "oridecon.ai.mcp.protocols",
    "PromptHandler": "oridecon.ai.mcp.server.handlers",
    "ResourceHandler": "oridecon.ai.mcp.server.handlers",
    "SSETransport": "oridecon.ai.mcp.transport",
    "SSEClientTransport": "oridecon.ai.mcp.client.core",
    "StdioClientTransport": "oridecon.ai.mcp.client.core",
    "StdioTransport": "oridecon.ai.mcp.transport",
    "ToolHandler": "oridecon.ai.mcp.server.handlers",
    "ToolRegistryAdapter": "oridecon.ai.mcp.adapters",
    "prompt": "oridecon.ai.mcp.decorators",
    "resource": "oridecon.ai.mcp.decorators",
    "tool": "oridecon.ai.mcp.decorators",
}


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        import importlib as _importlib

        module = _importlib.import_module(_LAZY_IMPORTS[name])
        value = getattr(module, name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = [
    "AbstractTransport",
    "ControllerPromptProvider",
    "ControllerResourceProvider",
    "ControllerToolProvider",
    "MCPClient",
    "MCPClientModule",
    "MCPClientProvider",
    "MCPClientRegistry",
    "MCPClientTransport",
    "MCPConfig",
    "MCPConnection",
    "MCPController",
    "MCPError",
    "MCPInitializationError",
    "MCPInitializeResult",
    "MCPJSONRPCRequest",
    "MCPJSONRPCResponse",
    "MCPMethodNotFoundError",
    "MCPModule",
    "MCPPrompt",
    "MCPPromptError",
    "MCPPromptHandlerProtocol",
    "MCPPromptMessage",
    "MCPPromptProviderProtocol",
    "MCPProtocolError",
    "MCPProvider",
    "MCPResource",
    "MCPResourceContent",
    "MCPResourceError",
    "MCPResourceHandlerProtocol",
    "MCPResourceProviderProtocol",
    "MCPServer",
    "MCPServerCapabilities",
    "MCPServerInfo",
    "MCPServerProtocol",
    "MCPServerStartedHook",
    "MCPServerStoppedHook",
    "MCPToolCallError",
    "MCPToolDefinition",
    "MCPToolHandlerProtocol",
    "MCPToolInvokedHook",
    "MCPToolProviderProtocol",
    "MCPTransportProtocol",
    "ModulePromptProvider",
    "ModuleResourceProvider",
    "ModuleToolProvider",
    "PromptHandler",
    "ResourceHandler",
    "SSEClientTransport",
    "SSETransport",
    "ServiceToolProvider",
    "StdioClientTransport",
    "StdioTransport",
    "ToolHandler",
    "ToolRegistryAdapter",
    "prompt",
    "resource",
    "tool",
]
