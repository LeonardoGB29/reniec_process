import pytest
from datetime import datetime
from domain.vital.model.Document import Document
from extensions import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# --------- FIXTURES PARA BD EN MEMORIA ---------

@pytest.fixture(scope="module")
def test_app():
    from flask import Flask
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope="function")
def session(test_app):
    with test_app.app_context():
        yield db.session
        db.session.rollback()



def test_create_document(session):
    doc = Document(number="123456", doc_type="DNI")
    session.add(doc)
    session.commit()

    fetched = Document.query.filter_by(number="123456").first()
    assert fetched is not None
    assert fetched.number == "123456"
    assert fetched.doc_type == "DNI"
    assert fetched.status == "PENDING"
    assert fetched.case_id is None
    assert isinstance(fetched.issued_at, datetime)

def test_change_status(session):
    doc = Document(number="654321", doc_type="PASSPORT", status="pending")
    session.add(doc)
    session.commit()

    doc.change_status("active")
    assert doc.status == "ACTIVE"
    assert doc.is_active() is True

def test_is_active_false(session):
    doc = Document(number="111222", doc_type="IDCARD", status="expired")
    session.add(doc)
    session.commit()

    assert doc.is_active() is False
