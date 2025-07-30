import pytest
from presentation.identityManagement.CaptureController import CaptureController

def test_capture_controller_instantiation():
    controller = CaptureController()
    assert isinstance(controller, CaptureController)
    assert controller.service is None

def test_capture_data_returns_none():
    controller = CaptureController()
    result = controller.capture_data(id=1)
    assert result is None

def test_get_captured_data_returns_none():
    controller = CaptureController()
    result = controller.get_captured_data(id=1)
    assert result is None
