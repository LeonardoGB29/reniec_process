#!/usr/bin/python
#-*- coding: utf-8 -*-

from domain.vital.model.Document import Document
from extensions import db

class SqlAlchemyDocumentRepository:
    def __init__(self):
        pass  # Puede inicializar algo si es necesario, como una sesión

    def add(self, document):
        """Añade un nuevo documento a la base de datos."""
        db.session.add(document)
        db.session.commit()
        return document

    def save(self, document):
        """Guarda o actualiza un documento existente."""
        db.session.add(document)  # Si es nuevo, lo agrega; si existe, lo actualiza
        db.session.commit()
        return document

    def find_by_id(self, document_id):
        """Busca un documento por su ID."""
        return db.session.get(Document, document_id)

    def find_by_person_id(self, person_id):
        """Busca documentos por el ID de una persona."""
        return db.session.query(Document).filter_by(case_id=person_id).all()

    # Alias para compatibilidad (opcional)
    def get_by_id(self, document_id):
        return self.find_by_id(document_id)

    def list_all(self):
        return db.session.query(Document).all()