import pytest
from domain.identityValidation.model.ValidationRequest import ValidationRequest

def test_validation_request_initial_state():
    vr = ValidationRequest()
    assert vr.dni is None
    assert vr.request_date is None

def test_getn_dni_returns_none():
    vr = ValidationRequest()
    result = vr.getn_dni()
    assert result is None

def test_get_request_date_returns_none():
    vr = ValidationRequest()
    result = vr.get_request_date()
    assert result is None
