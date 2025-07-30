import pytest
from domain.identityManagement.model.IdentityRequest import IdentityRequest

def test_identity_request_initial_state():
    req = IdentityRequest()
    assert req.dni is None
    assert req.created_at is None

def test_get_dni_returns_none():
    req = IdentityRequest()
    result = req.get_dni()
    assert result is None
