import pytest
from domain.actualization.service.BiometricoService import BiometricoService

class DummyBiometric:
    # Clase simulada para representar un objeto biometric
    pass

def test_biometrico_service_can_be_instantiated():
    service = BiometricoService()
    assert isinstance(service, BiometricoService)

def test_biometrico_service_save_does_nothing():
    service = BiometricoService()
    biometric = DummyBiometric()
    result = service.save(biometric)
    assert result is None
