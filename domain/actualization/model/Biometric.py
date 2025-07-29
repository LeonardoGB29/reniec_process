#!/usr/bin/python
#-*- coding: utf-8 -*-

class Biometric:
    def __init__(self):
        self.biometricType = None
        self.encodedData: String  = None
        self.captureDate: Date = None
        self.qualityScore: float = None
        self.deviceId: String = None

    def isValid(): boolean(self, ):
        # Método intencionalmente vacío. No se requiere lógica por ahora.
        pass

    def getBiometricHash(): String(self, ):
        # Método intencionalmente vacío. No se requiere lógica por ahora.
        pass

