#!/usr/bin/python
#-*- coding: utf-8 -*-

class RequestServiceImpl:
    def __init__(self):
        self.repo = None

    def send(self, req):
        raise NotImplementedError("El método 'send' aún no está implementado.")
        pass

    def status(self, id):
        # Método intencionalmente vacío. No se requiere lógica por ahora.
        pass

