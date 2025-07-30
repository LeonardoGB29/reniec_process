from flask import Blueprint, request, jsonify
from extensions import db
from domain.vital.model.VitalObservation import VitalObservation

class ObservationService:
    def __init__(self, repo=None):
        self.repo = repo if repo else db  # Usa db.session si no hay repo definido

    def create(self, document_id, title, description):
        """Crea una nueva observación asociada a un documento."""
        observation = VitalObservation(
            title=title,
            description=description,
            document_id=document_id
        )
        if self.repo == db:
            db.session.add(observation)
            db.session.commit()
        else:
            self.repo.add(observation)
        return observation

    def get(self, observation_id):
        """Obtiene una observación por su ID."""
        if self.repo == db:
            return db.session.get(VitalObservation, observation_id)
        return self.repo.get_by_id(observation_id)

    def list_by_document_id(self, document_id):
        """Lista todas las observaciones asociadas a un documento."""
        if self.repo == db:
            return db.session.query(VitalObservation).filter_by(document_id=document_id).all()
        return self.repo.list_by_document_id(document_id)

    def associate_to_document(self, observation_id, document_id):
        """Asocia una observación a un documento."""
        obs = self.get(observation_id)
        if not obs:
            raise ValueError("Observation not found")
        obs.document_id = document_id
        if self.repo == db:
            db.session.commit()
        else:
            self.repo.update(obs)
        return obs
