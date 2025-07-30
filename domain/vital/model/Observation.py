from extensions import db
from datetime import datetime

class Observation(db.Model):
    __tablename__ = 'observations'

    id = db.Column(db.Integer, primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey('document.id'), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default="PENDING")

    def __init__(self, document_id, description, status=None):
        self.document_id = document_id
        self.description = description
        self.status = status or "PENDING"  # Usa "PENDING" si no se proporciona un estado
