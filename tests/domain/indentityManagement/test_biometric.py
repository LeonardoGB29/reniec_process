import pytest
from datetime import date
from domain.actualization.model.Biometric import Biometric

def test_biometric_initial_state():
    bio = Biometric()
    assert bio.biometric_type is None
    assert bio.encoded_data is None
    assert bio.capture_date is None
    assert bio.quality_score is None
    assert bio.device_id is None

def test_is_valid_returns_none():
    bio = Biometric()
    assert bio.is_valid() is None

def test_get_biometric_hash_returns_none():
    bio = Biometric()
    assert bio.get_biometric_hash() is None
