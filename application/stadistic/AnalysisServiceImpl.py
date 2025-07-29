#!/usr/bin/python
#-*- coding: utf-8 -*-

class AnalysisServiceImpl:
    def __init__(self):
        self.repo = None

    def process_data(self, filters):
        raise NotImplementedError("El método 'process_data' aún no está implementado.")

    def check_integrity(self, result_id):
        # Método intencionalmente vacío. No se requiere lógica por ahora.
        pass

