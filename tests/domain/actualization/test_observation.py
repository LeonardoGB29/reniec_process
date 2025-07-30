import pytest
from domain.actualization.model.Observation import Observation 

def test_observation_initial_state():
    obs = Observation()
    assert obs.id is None
    assert obs.related_person_id is None
    assert obs.comment is None

def test_summarize_returns_none_when_not_implemented():
    obs = Observation()
    assert obs.summarize() is None

def test_is_critical_returns_none_when_not_implemented():
    obs = Observation()
    assert obs.is_critical() is None
