#!/usr/bin/python
#-*- coding: utf-8 -*-

class NotificationServiceImpl:
    def __init__(self):
        self.repo = None

    def notifyObservation(self, id, obs):
        # Método intencionalmente vacío. No se requiere lógica por ahora.
        pass

    def notifyResult(self, id, status):
        raise NotImplementedError("El método 'notifyResult' aún no está implementado.")

