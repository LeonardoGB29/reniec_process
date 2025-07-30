#!/usr/bin/python
#-*- coding: utf-8 -*-

from datetime import date
from typing import Optional

class Biometric:
    def __init__(self):
        self.biometric_type = None
        self.encoded_data: Optional[str] = None
        self.capture_date: Optional[date] = None
        self.quality_score: Optional[float] = None
        self.device_id: Optional[str] = None
        
    def is_valid(self) -> bool:
        # Método intencionalmente vacío. No se requiere lógica por ahora.
        pass

    def get_biometric_hash(self) -> str:
        # Método intencionalmente vacío. No se requiere lógica por ahora.
        pass
