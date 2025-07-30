from extensions import db

class VitalCase(db.Model):
    __tablename__ = 'vital_cases'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True)  # Clave primaria
    person_id = db.Column(db.String(8), nullable=False)  # Cambiado a String para almacenar el DNI
    status = db.Column(db.String(50), default='PENDING')  # Estado del caso (PENDING, RESOLVED, CANCELED)

    def __repr__(self):
        return f"<VitalCase {self.id} - person_id={self.person_id} - status={self.status}>"
