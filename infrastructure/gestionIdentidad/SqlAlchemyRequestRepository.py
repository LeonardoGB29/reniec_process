#!/usr/bin/python
#-*- coding: utf-8 -*-

from domain.identityManagement.repository.RequestRepository import RequestRepository

class SqlAlchemyRequestRepository(RequestRepository):
    def __init__(self):
        pass

    def save(self, request):
        pass

    def findById(self, requestId):
        pass

    def updateStatus(self, requestId, status):
        pass

