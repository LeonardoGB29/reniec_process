#!/usr/bin/python
#-*- coding: utf-8 -*-

class ValidationServiceImpl:
    def __init__(self):
        self.repo = None

    def check_structure(self, id):
        # Método intencionalmente vacío. No se requiere lógica por ahora.
        pass

    def check_biometrics(self, id):
        raise NotImplementedError("El método 'checkBiometrics' aún no está implementado.")

