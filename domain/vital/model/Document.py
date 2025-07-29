from extensions import db
from datetime import datetime

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(50), nullable=False)
    doc_type = db.Column(db.String(30), nullable=False)
    issued_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default="PENDING")
    case_id = db.Column(db.Integer, nullable=True)

    def __init__(self):
        self.id_acta = None
        self.doc_type = None
        self.issued_at = None
        self.status = None

    def change_status(self, new_status):
        # Método intencionalmente vacío. No se requiere lógica por ahora.
        pass

    def is_active(self, ):
        # Método intencionalmente vacío. No se requiere lógica por ahora.
        pass

