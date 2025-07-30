from extensions import db
from datetime import datetime

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20), nullable=False)  # Número del documento
    doc_type = db.Column(db.String(30), nullable=False)  # Tipo de documento
    issued_at = db.Column(db.DateTime, default=datetime.utcnow)  # Fecha de emisión
    status = db.Column(db.String(20), default="PENDING")  # Estado del documento
    case_id = db.Column(db.Integer, db.ForeignKey('vital_cases.id'), nullable=True)  # Relación con VitalCase
    person_id = db.Column(db.String(8), nullable=True)  # DNI de la persona

    def __init__(self, number, doc_type, status=None, case_id=None, person_id=None):
        self.number = number
        self.doc_type = doc_type
        self.status = status or "PENDING"  # Usa el default si no se pasa
        self.case_id = case_id
        self.person_id = person_id

    def change_status(self, new_status):
        self.status = new_status.upper()  # Cambia el estado del documento

    def is_active(self):
        return self.status.upper() == "ACTIVE"  # Verifica si el documento está activo
