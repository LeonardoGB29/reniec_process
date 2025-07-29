from domain.vital.model.Document import Document
from extensions import db

class DocumentService:
    def __init__(self, repo=None):
        self.repo = repo if repo else db

    def register(self, data):
        doc = Document(
            number=data["number"],
            doc_type=data["doc_type"],
            case_id=data.get("case_id"),
            status=data.get("status", "PENDING") 
        )
        if self.repo == db:
            db.session.add(doc)
            db.session.commit()
        else:
            self.repo.add(doc)
        return doc

    def get(self, doc_id):
        if self.repo == db:
            return db.session.get(Document, doc_id)
        return self.repo.get_by_id(doc_id)

    def list(self):
        if self.repo == db:
            return db.session.query(Document).all()
        return self.repo.list_all()

    def change_status(self, doc_id, new_status):
        doc = self.get(doc_id)
        if not doc:
            raise ValueError("Document not found")
        doc.change_status(new_status.upper())
        if self.repo == db:
            db.session.commit()
        else:
            self.repo.update(doc)
        return doc
