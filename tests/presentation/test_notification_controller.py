import pytest
from presentation.identityValidation.NotificationController import NotificationController 

def test_controller_instantiation():
    controller = NotificationController()
    assert isinstance(controller, NotificationController)
    assert controller.service is None

def test_send_observation_returns_none():
    controller = NotificationController()
    result = controller.send_observation(123, "Observación de prueba")
    assert result is None

def test_send_result_returns_none():
    controller = NotificationController()
    result = controller.send_result(456, "COMPLETED")
    assert result is None
