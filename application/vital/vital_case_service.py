from domain.vital.model.vital_case import VitalCase
from infrastructure.vital.sqlalchemy_vital_case_repository import SqlAlchemyVitalCaseRepository

class VitalCaseService:
    def __init__(self):
        self.repo = SqlAlchemyVitalCaseRepository()

    def create_case(self, data):
        case = VitalCase(person_id=data["person_id"])
        return self.repo.add(case)

    def get_case(self, case_id):
        return self.repo.get_by_id(case_id)

    def list_cases(self):
        return self.repo.list_all()

    def update_status(self, case_id, new_status):
        return self.repo.update_status(case_id, new_status)
