import pytest
from domain.identityValidation.model.BiometricData import BiometricData

def test_biometric_data_instantiation():
    bio = BiometricData()
    assert bio.image_hash is None
    assert bio.capture_time is None

def test_is_valid_returns_none():
    bio = BiometricData()
    result = bio.is_valid()
    assert result is None
