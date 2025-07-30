import pytest
from domain.identityValidation.model.ValidationResult import ValidationResult

def test_validation_result_initial_state():
    vr = ValidationResult()
    assert vr.status is None
    assert vr.reason is None

def test_is_approved_returns_none():
    vr = ValidationResult()
    result = vr.is_approved()
    assert result is None
