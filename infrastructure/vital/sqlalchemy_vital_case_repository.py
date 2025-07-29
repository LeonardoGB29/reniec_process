from domain.vital.model.vital_case import VitalCase
from extensions import db

class SqlAlchemyVitalCaseRepository:
    def add(self, case):
        db.session.add(case)
        db.session.commit()
        return case

    def get_by_id(self, case_id):
        return VitalCase.query.get(case_id)

    def list_all(self):
        return VitalCase.query.all()

    def update_status(self, case_id, new_status):
        case = self.get_by_id(case_id)
        if case:
            case.status = new_status
            db.session.commit()
        return case
