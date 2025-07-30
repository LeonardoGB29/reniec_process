import pytest
from extensions import db
from flask import Flask
from domain.vital.model.Document import Document
from application.vital.document_service import DocumentService

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def real_service(app):
    return DocumentService(repo=db)



def test_register_with_db(real_service):
    data = {
        "number": "777777",
        "doc_type": "RUC"
    }
    doc = real_service.register(data)
    assert doc.id is not None
    assert doc.status == "PENDING"

def test_change_status_with_db(real_service):
    doc = real_service.register({"number": "DB123", "doc_type": "ID"})
    updated = real_service.change_status(doc.id, "active")
    assert updated.status == "ACTIVE"






# Repositorio mock
class MockRepo:
    def __init__(self):
        self.storage = {}
        self.counter = 1

    def add(self, doc):
        doc.id = self.counter
        self.storage[self.counter] = doc
        self.counter += 1

    def get_by_id(self, doc_id):
        return self.storage.get(doc_id)

    def list_all(self):
        return list(self.storage.values())

    def update(self, doc):
        self.storage[doc.id] = doc

# Fixture para el servicio con repo simulado
@pytest.fixture
def service():
    return DocumentService(repo=MockRepo())

def test_register_document(service):
    data = {
        "number": "123456",
        "doc_type": "DNI"
    }
    doc = service.register(data)
    assert doc.number == "123456"
    assert doc.doc_type == "DNI"
    assert doc.status == "PENDING"
    assert doc.id == 1

def test_get_document(service):
    data = {
        "number": "654321",
        "doc_type": "PASSPORT"
    }
    doc = service.register(data)
    fetched = service.get(doc.id)
    assert fetched is not None
    assert fetched.number == "654321"

def test_list_documents(service):
    service.register({"number": "A1", "doc_type": "DNI"})
    service.register({"number": "B2", "doc_type": "DNI"})
    all_docs = service.list()
    assert len(all_docs) == 2

def test_change_status(service):
    doc = service.register({"number": "XYZ123", "doc_type": "IDCARD"})
    
    # El método change_status en Document no debe usar db.session.commit() directamente en este contexto
    updated = service.change_status(doc.id, "active")
    
    assert updated.status == "ACTIVE"
    assert updated.is_active() is True


def test_change_status_not_found(service):
    with pytest.raises(ValueError, match="Document not found"):
        service.change_status(999, "inactive")


def test_register_with_status_and_case_id(service):
    data = {
        "number": "999999",
        "doc_type": "LICENSE",
        "status": "APPROVED",
        "case_id": 101
    }
    doc = service.register(data)
    assert doc.status == "APPROVED"
    assert doc.case_id == 101

def test_get_document_not_found(service):
    doc = service.get(999)
    assert doc is None


def test_document_is_active(service):
    doc = service.register({"number": "ZZZ", "doc_type": "CARD"})
    doc.change_status("ACTIVE")
    assert doc.is_active()


def test_list_documents_empty(service):
    assert service.list() == []
