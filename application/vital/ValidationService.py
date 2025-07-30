from datetime import datetime
from typing import Tuple

class ValidationService:
    @staticmethod
    def validate_document(data: dict) -> Tuple[bool, str]:
        """Valida los datos básicos de un documento"""
        required_fields = ['number', 'doc_type', 'case_id']
        for field in required_fields:
            if field not in data:
                return False, f"Campo requerido faltante: {field}"
        
        if data['doc_type'].lower() not in ['birth', 'marriage', 'death']:
            return False, "Tipo de documento inválido"
        
        return True, "Documento válido"
    
    @staticmethod
    def validate_acta(acta_text: str) -> Tuple[bool, str]:
        """Valida el texto de un acta"""
        if len(acta_text.strip()) < 10:
            return False, "El texto del acta es demasiado corto"
        return True, "Acta válida"
    
    @staticmethod
    def validate_requirements(document_id: int) -> Tuple[bool, str]:
        """Valida los requisitos completos de un documento"""
        # Aquí puedes implementar lógica de validación más compleja
        if not document_id or document_id < 1:
            return False, "ID de documento inválido"
        return True, "Todos los requisitos cumplidos"
    
    @staticmethod
    def is_completed_in_time(created_at: datetime, days_limit: int = 30) -> bool:
        """Verifica si un trámite se completó en el tiempo establecido"""
        return (datetime.utcnow() - created_at).days <= days_limit
