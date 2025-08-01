from extensions import db
from datetime import datetime

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20), nullable=False)
    doc_type = db.Column(db.String(30), nullable=False)
    issued_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default="PENDING")
    case_id = db.Column(db.Integer, nullable=True)

    def __init__(self, number, doc_type, status=None, case_id=None):
        self.number = number
        self.doc_type = doc_type
        self.status = status
        self.case_id = case_id

    def change_status(self, new_status):
        self.status = new_status.upper()

    def is_active(self):
        return self.status.upper() == "ACTIVE"
