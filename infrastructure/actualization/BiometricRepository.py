#!/usr/bin/python
#-*- coding: utf-8 -*-

from BiometricoRepository import BiometricoRepository

class BiometricRepository(BiometricoRepository):
    def __init__(self):
        super().__init__()
        # Constructor intencionalmente vacío porque no aplica a este repositorio

    def save(self, biometric):
        # Override intencionalmente vacío porque no aplica a este repositorio
        pass

    def deleteByPersonId(self, personId):
        # Método intencionalmente vacío. No se requiere lógica por ahora.
        pass

    def update(self, biometric):
        # Método intencionalmente vacío. No se requiere lógica por ahora.
        pass

