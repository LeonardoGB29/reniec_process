import pytest
from domain.identityValidation.ValidationRepository import ValidationRepository 

def test_validation_repository_initial_state():
    repo = ValidationRepository()
    assert repo.attribute1 is None
