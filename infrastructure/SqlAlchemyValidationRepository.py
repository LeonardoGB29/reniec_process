#!/usr/bin/python
#-*- coding: utf-8 -*-

from domain.identityValidation.ValidationRepository import ValidationRepository

class SqlAlchemyValidationRepository(ValidationRepository):
    def __init__(self):
        pass

    def save(self, validation):
        pass

    def findByRequestId(self, requestId):
        pass

    def findAllByPersonId(self, personId):
        pass

