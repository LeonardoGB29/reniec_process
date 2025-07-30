from extensions import db
from domain.vital.model.Document import Document
from domain.vital.model.Observation import Observation
from domain.vital.model.Acta import Acta
from typing import List, Optional

class DataService:
    def __init__(self, db_session=None):
        self.db = db_session or db
    
    # Operaciones CRUD para Documentos
    def create_document(self, data: dict) -> Document:
        """Crea un nuevo documento en la base de datos"""
        document = Document(**data)
        self.db.session.add(document)
        self.db.session.commit()
        return document
    
    def get_document(self, doc_id: int) -> Optional[Document]:
        """Obtiene un documento por su ID"""
        return self.db.session.get(Document, doc_id)
    
    def update_document(self, doc_id: int, update_data: dict) -> Optional[Document]:
        """Actualiza un documento existente"""
        document = self.get_document(doc_id)
        if document:
            for key, value in update_data.items():
                setattr(document, key, value)
            self.db.session.commit()
        return document
    
    # Operaciones para Observations
    def create_observation(self, document_id: int, description: str) -> Observation:
        """Crea una nueva observación"""
        observation = Observation(document_id=document_id, description=description)
        self.db.session.add(observation)
        self.db.session.commit()
        return observation
    
    def get_observations_by_document(self, document_id: int) -> List[Observation]:
        """Obtiene todas las observaciones de un documento"""
        return self.db.session.query(Observation).filter_by(document_id=document_id).all()
    
    # Operaciones para Actas
    def create_acta(self, data: dict) -> Acta:
        """Crea una nueva acta"""
        acta = Acta(**data)
        self.db.session.add(acta)
        self.db.session.commit()
        return acta
    
    def get_acta(self, acta_id: int) -> Optional[Acta]:
        """Obtiene un acta por su ID"""
        return self.db.session.get(Acta, acta_id)
    
    def get_all_documents(self) -> List[Document]:
        """Obtiene todos los documentos"""
        return self.db.session.query(Document).all()
    
    def delete_document(self, doc_id: int) -> bool:
        """Elimina un documento"""
        document = self.get_document(doc_id)
        if document:
            self.db.session.delete(document)
            self.db.session.commit()
            return True
        return False
