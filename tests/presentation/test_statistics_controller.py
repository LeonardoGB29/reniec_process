import pytest
from presentation.stadistic.StatisticsController import StatisticsController 

def test_statistics_controller_instantiation():
    controller = StatisticsController()
    assert controller.service is None
    assert controller.attribute1 is None
    assert controller.attribute2 is None
    assert controller.attribute3 is None

def test_validate_request_returns_none():
    controller = StatisticsController()
    dummy_request = {"data": "test"}
    result = controller.validate_request(dummy_request)
    assert result is None

def test_check_permissions_returns_none():
    controller = StatisticsController()
    result = controller.check_permissions(user_id=1)
    assert result is None
