from extensions import db
from domain.vital.model.Document import Document

class SqlAlchemyDocumentRepository:
    def add(self, doc: Document):
        db.session.add(doc)
        db.session.commit()

    def get_by_id(self, doc_id: int) -> Document | None:
        return db.session.get(Document, doc_id)

    def list_all(self) -> list[Document]:
        return Document.query.all()

    def update(self):
        db.session.commit()
