import pytest
from domain.identityValidation.service.ValidationService import ValidationService

class DummyRequest:
    pass

class DummyValidation:
    pass

def test_validation_service_initial_state():
    service = ValidationService()
    assert service.validation_repository is None
    assert service.attribute1 is None

def test_validate_request_runs_without_error():
    service = ValidationService()
    req = DummyRequest()
    result = service.validate_request(req)
    assert result is None  # Método vacío no retorna nada

def test_log_validation_runs_without_error():
    service = ValidationService()
    val = DummyValidation()
    result = service.log_validation(val)
    assert result is None  # Método vacío no retorna nada
