import pytest
from domain.identityManagement.model.CapturedBiometric import CapturedBiometric

def test_captured_biometric_initial_state():
    cb = CapturedBiometric()
    assert cb.type is None
    assert cb.data is None

def test_is_valid_returns_none():
    cb = CapturedBiometric()
    assert cb.is_valid() is None
