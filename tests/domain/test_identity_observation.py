import pytest
from domain.identityValidation.model.Observation import Observation 

def test_observation_instantiation():
    obs = Observation()
    assert obs.text is None
    assert obs.created_at is None
    assert obs.port1 is None

def test_get_text_returns_none():
    obs = Observation()
    result = obs.get_text()
    assert result is None
