from extensions import db
from domain.vital.model.Acta import Acta
from typing import Optional, List, Dict
from datetime import datetime

class ActaService:
    def __init__(self, repository=None):
        self.repository = repository or db  # Permite inyección para testing
    
    def create_acta(self, document_id: int, acta_texto: str, status: str = "PENDING") -> Acta:
        """
        Crea un nuevo acta en el sistema.
        
        Args:
            document_id: ID del documento asociado
            acta_texto: Contenido textual del acta
            status: Estado inicial (default: "PENDING")
        
        Returns:
            Instancia de Acta creada
        """
        if not acta_texto or len(acta_texto.strip()) < 10:
            raise ValueError("El texto del acta es demasiado corto o vacío")
        
        new_acta = Acta(
            document_id=document_id,
            acta_texto=acta_texto,
            status=status
        )
        
        if self.repository == db:
            db.session.add(new_acta)
            db.session.commit()
        else:
            self.repository.add(new_acta)
            
        return new_acta
    
    def get_by_id(self, acta_id: int) -> Optional[Acta]:
        """Recupera un acta por su ID"""
        if self.repository == db:
            return db.session.get(Acta, acta_id)
        return self.repository.get_by_id(acta_id)
    
    def get_by_document(self, document_id: int) -> List[Acta]:
        """Lista todas las actas asociadas a un documento"""
        if self.repository == db:
            return db.session.query(Acta).filter_by(document_id=document_id).all()
        return self.repository.list_by_document_id(document_id)
    
    def update_text(self, acta_id: int, new_text: str) -> Optional[Acta]:
        """Actualiza el texto de un acta existente"""
        acta = self.get_by_id(acta_id)
        if acta:
            acta.acta_texto = new_text
            acta.updated_at = datetime.utcnow()
            if self.repository == db:
                db.session.commit()
            else:
                self.repository.update(acta)
        return acta
    
    def change_status(self, acta_id: int, new_status: str) -> Optional[Acta]:
        """Cambia el estado de un acta (ej: 'APPROVED', 'REJECTED')"""
        valid_statuses = {"PENDING", "APPROVED", "REJECTED", "ARCHIVED"}
        if new_status not in valid_statuses:
            raise ValueError(f"Estado inválido. Use uno de: {valid_statuses}")
        
        acta = self.get_by_id(acta_id)
        if acta:
            acta.status = new_status
            if self.repository == db:
                db.session.commit()
            else:
                self.repository.update(acta)
        return acta
    
    def get_all_actas(self) -> List[Acta]:
        """Obtiene todas las actas del sistema"""
        if self.repository == db:
            return db.session.query(Acta).all()
        return self.repository.get_all()
    
    def delete_acta(self, acta_id: int) -> bool:
        """Elimina un acta del sistema"""
        acta = self.get_by_id(acta_id)
        if acta:
            if self.repository == db:
                db.session.delete(acta)
                db.session.commit()
            else:
                self.repository.delete(acta)
            return True
        return False
