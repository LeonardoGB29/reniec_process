from extensions import db
from datetime import datetime

class Acta(db.Model):
    __tablename__ = 'actas'

    id = db.Column(db.Integer, primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey('document.id'), nullable=False)
    acta_texto = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default="PENDING")

    def __init__(self, document_id, acta_texto, status=None):
        self.document_id = document_id
        self.acta_texto = acta_texto
        self.status = status or "PENDING"  # Usa "PENDING" si no se proporciona un estado
