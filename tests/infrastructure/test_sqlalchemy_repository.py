import pytest
from flask import Flask
from extensions import db
from domain.vital.model.Document import Document
from infrastructure.vital.SqlAlchemyDocumentRepository import SqlAlchemyDocumentRepository  # Asegúrate de que la ruta sea correcta


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
def repo(app):
    return SqlAlchemyDocumentRepository()


def test_add_document(repo):
    doc = Document(number="111", doc_type="DNI", status="PENDING")
    added = repo.add(doc)
    assert added.id is not None
    assert added.number == "111"
    assert added.status == "PENDING"


def test_save_document(repo):
    doc = Document(number="222", doc_type="PASSPORT", status="PENDING")
    repo.add(doc)
    doc.status = "ACTIVE"
    saved = repo.save(doc)
    assert saved.status == "ACTIVE"


def test_find_by_id(repo):
    doc = Document(number="333", doc_type="RUC")
    repo.add(doc)
    found = repo.find_by_id(doc.id)
    assert found is not None
    assert found.number == "333"


def test_get_by_id(repo):
    doc = Document(number="444", doc_type="IDCARD")
    repo.add(doc)
    found = repo.get_by_id(doc.id)
    assert found is not None
    assert found.number == "444"


def test_find_by_person_id(repo):
    doc1 = Document(number="A1", doc_type="DNI", case_id=999)
    doc2 = Document(number="A2", doc_type="RUC", case_id=999)
    doc3 = Document(number="B1", doc_type="DNI", case_id=1000)
    repo.add(doc1)
    repo.add(doc2)
    repo.add(doc3)

    results = repo.find_by_person_id(999)
    assert len(results) == 2
    assert all(d.case_id == 999 for d in results)


def test_list_all(repo):
    repo.add(Document(number="L1", doc_type="DNI"))
    repo.add(Document(number="L2", doc_type="PASSPORT"))
    docs = repo.list_all()
    assert len(docs) == 2
    numbers = [doc.number for doc in docs]
    assert "L1" in numbers and "L2" in numbers
