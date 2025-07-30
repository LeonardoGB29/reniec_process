import pytest
from domain.identityManagement.model.DNIDelivery import DNIDelivery 

class DummyDoc:
    pass

def test_dni_delivery_initial_state():
    delivery = DNIDelivery()
    assert delivery.delivery_repository is None
    assert delivery.attribute1 is None

def test_deliver_method_runs_without_error():
    delivery = DNIDelivery()
    doc = DummyDoc()
    result = delivery.deliver(doc)
    assert result is None  # Porque deliver no retorna nada aún
