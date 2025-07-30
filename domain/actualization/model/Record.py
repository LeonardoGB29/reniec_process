#!/usr/bin/python
#-*- coding: utf-8 -*-

from typing import Optional

class Record:
    def __init__(self):
        self.id = None
        self.person_id: Optional[str] = None
        self.comment = None

    def is_successful(self, ):
        # Método intencionalmente vacío. No se requiere lógica por ahora.
        pass

    def get_summary(self, ):
        # Método intencionalmente vacío. No se requiere lógica por ahora.
        pass

