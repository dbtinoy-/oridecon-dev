"""Tests for validation/__init__ module."""
import pytest


class TestValidationLazyImports:
    """Tests for validation module lazy imports."""

    def test_lazy_import_field_error(self) -> None:
        """Test lazy import of FieldError."""
        from oridecon.validation import FieldError
        assert FieldError is not None

    def test_lazy_import_validate_input(self) -> None:
        """Test lazy import of validate_input."""
        from oridecon.validation import validate_input
        assert callable(validate_input)

    def test_lazy_import_field(self) -> None:
        """Test lazy import of Field."""
        from oridecon.validation import Field
        assert Field is not None

    def test_lazy_import_config_dict(self) -> None:
        """Test lazy import of ConfigDict."""
        from oridecon.validation import ConfigDict
        assert ConfigDict is not None

    def test_lazy_import_email_str(self) -> None:
        """Test lazy import of EmailStr."""
        from oridecon.validation import EmailStr
        assert EmailStr is not None

    def test_lazy_import_http_url(self) -> None:
        """Test lazy import of HttpUrl."""
        from oridecon.validation import HttpUrl
        assert HttpUrl is not None

    def test_lazy_import_secret_str(self) -> None:
        """Test lazy import of SecretStr."""
        from oridecon.validation import SecretStr
        assert SecretStr is not None

    def test_lazy_import_field_validator(self) -> None:
        """Test lazy import of field_validator."""
        from oridecon.validation import field_validator
        assert callable(field_validator)

    def test_lazy_import_model_validator(self) -> None:
        """Test lazy import of model_validator."""
        from oridecon.validation import model_validator
        assert callable(model_validator)

    def test_lazy_import_abstract_rule(self) -> None:
        """Test lazy import of AbstractRule."""
        from oridecon.validation import AbstractRule
        assert AbstractRule is not None

    def test_lazy_import_abstract_async_rule(self) -> None:
        """Test lazy import of AbstractAsyncRule."""
        from oridecon.validation import AbstractAsyncRule
        assert AbstractAsyncRule is not None

    def test_lazy_import_required(self) -> None:
        """Test lazy import of Required."""
        from oridecon.validation import Required
        assert Required is not None

    def test_lazy_import_min_length(self) -> None:
        """Test lazy import of MinLength."""
        from oridecon.validation import MinLength
        assert MinLength is not None

    def test_lazy_import_max_length(self) -> None:
        """Test lazy import of MaxLength."""
        from oridecon.validation import MaxLength
        assert MaxLength is not None

    def test_lazy_import_pattern(self) -> None:
        """Test lazy import of Pattern."""
        from oridecon.validation import Pattern
        assert Pattern is not None

    def test_lazy_import_range(self) -> None:
        """Test lazy import of Range."""
        from oridecon.validation import Range
        assert Range is not None

    def test_lazy_import_one_of(self) -> None:
        """Test lazy import of OneOf."""
        from oridecon.validation import OneOf
        assert OneOf is not None

    def test_lazy_import_email_format(self) -> None:
        """Test lazy import of EmailFormat."""
        from oridecon.validation import EmailFormat
        assert EmailFormat is not None

    def test_lazy_import_custom(self) -> None:
        """Test lazy import of Custom."""
        from oridecon.validation import Custom
        assert Custom is not None

    def test_lazy_import_required_func(self) -> None:
        """Test lazy import of required function."""
        from oridecon.validation import required
        assert callable(required)

    def test_lazy_import_min_length_func(self) -> None:
        """Test lazy import of min_length function."""
        from oridecon.validation import min_length
        assert callable(min_length)

    def test_lazy_import_max_length_func(self) -> None:
        """Test lazy import of max_length function."""
        from oridecon.validation import max_length
        assert callable(max_length)

    def test_lazy_import_pattern_func(self) -> None:
        """Test lazy import of pattern function."""
        from oridecon.validation import pattern
        assert callable(pattern)

    def test_lazy_import_range_check_func(self) -> None:
        """Test lazy import of range_check function."""
        from oridecon.validation import range_check
        assert callable(range_check)

    def test_lazy_import_one_of_func(self) -> None:
        """Test lazy import of one_of function."""
        from oridecon.validation import one_of
        assert callable(one_of)

    def test_lazy_import_email_format_func(self) -> None:
        """Test lazy import of email_format function."""
        from oridecon.validation import email_format
        assert callable(email_format)

    def test_lazy_import_custom_func(self) -> None:
        """Test lazy import of custom function."""
        from oridecon.validation import custom
        assert callable(custom)

    def test_lazy_import_validator(self) -> None:
        """Test lazy import of ValidatorImpl."""
        from oridecon.validation import ValidatorImpl
        assert ValidatorImpl is not None

    def test_lazy_import_async_validator(self) -> None:
        """Test lazy import of AsyncValidator."""
        from oridecon.validation import AsyncValidator
        assert AsyncValidator is not None

    def test_lazy_import_validation_config(self) -> None:
        """Test lazy import of ValidationConfig."""
        from oridecon.validation import ValidationConfig
        assert ValidationConfig is not None

    def test_lazy_import_validation_error(self) -> None:
        """Test lazy import of ValidationError."""
        from oridecon.validation import ValidationError
        assert ValidationError is not None


class TestValidationDir:
    """Tests for validation.__dir__()."""

    def test_dir_includes_lazy_imports(self) -> None:
        """Test __dir__ returns all lazy import keys."""
        from oridecon import validation
        d = dir(validation)
        assert "ValidatorImpl" in d
        assert "Required" in d

    def test_all_in_dir_are_in_all(self) -> None:
        """Test __all__ matches __dir__."""
        from oridecon import validation
        assert set(dir(validation)) == set(validation.__all__)


class TestValidationAttributeError:
    """Tests for validation module error handling."""

    def test_raises_attribute_error_for_unknown(self) -> None:
        """Test that unknown attributes raise AttributeError."""
        from oridecon import validation
        with pytest.raises(AttributeError, match="has no attribute"):
            validation.nonexistent_attribute