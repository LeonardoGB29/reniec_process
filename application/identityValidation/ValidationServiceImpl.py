#!/usr/bin/python
#-*- coding: utf-8 -*-

class ValidationServiceImpl:
    def __init__(self):
        self.repo = None

    def checkStructure(self, id):
        # Método intencionalmente vacío. No se requiere lógica por ahora.
        pass

    def checkBiometrics(self, id):
        raise NotImplementedError("El método 'checkBiometrics' aún no está implementado.")

