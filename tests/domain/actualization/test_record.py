import pytest
from domain.actualization.model.Record import Record

def test_record_initial_state():
    record = Record()
    assert record.id is None
    assert record.person_id is None
    assert record.comment is None

def test_is_successful_returns_none():
    record = Record()
    assert record.is_successful() is None

def test_get_summary_returns_none():
    record = Record()
    assert record.get_summary() is None
