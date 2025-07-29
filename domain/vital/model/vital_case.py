from extensions import db

class VitalCase(db.Model):
    __tablename__ = 'vital_cases'

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), default='PENDING')  # Otros: RESOLVED, CANCELED

    def __repr__(self):
        return f"<VitalCase {self.id} - person_id={self.person_id} - status={self.status}>"
