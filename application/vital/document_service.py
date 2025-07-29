from domain.vital.model.document import Document
from extensions import db

class DocumentService:
    def __init__(self, repo):
        self.repo = repo

    def register(self, data):
        doc = Document(
            number=data["number"],
            doc_type=data["doc_type"],
            case_id=data.get("case_id")
        )
        self.repo.add(doc)
        return doc

    def get(self, doc_id):
        return self.repo.get_by_id(doc_id)

    def list(self):
        return self.repo.list_all()

    def change_status(self, doc_id, new_status):
        doc = self.repo.get_by_id(doc_id)

        if not doc:
            raise ValueError("Document not found")
        
        doc.status = new_status.upper()
        self.repo.update(doc)
        return doc
