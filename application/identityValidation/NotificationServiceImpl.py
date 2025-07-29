#!/usr/bin/python
#-*- coding: utf-8 -*-

class NotificationServiceImpl:
    def __init__(self):
        self.repo = None

    def notify_observation(self, id, obs):
        # Método intencionalmente vacío. No se requiere lógica por ahora.
        pass

    def notify_result(self, id, status):
        raise NotImplementedError("El método 'notifyResult' aún no está implementado.")

