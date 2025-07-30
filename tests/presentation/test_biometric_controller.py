import pytest
from presentation.actualization.BiometricController import BiometricController

def test_controller_instantiation():
    controller = BiometricController()
    assert isinstance(controller, BiometricController)

def test_method_exists():
    controller = BiometricController()
    assert hasattr(controller, 'get_biometric_by_person')

def test_get_biometric_by_person_returns_none():
    controller = BiometricController()
    result = controller.get_biometric_by_person(1)
    assert result is None
