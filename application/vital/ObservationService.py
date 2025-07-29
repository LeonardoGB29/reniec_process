from flask import Blueprint, request, jsonify
from extensions import db
from domain.vital.model.VitalObservation import VitalObservation

class ObservationService:

    @staticmethod
    def create_observation(data):
        obs = VitalObservation(
            title=data['title'],
            description=data['description'],
            document_id=data['document_id']
        )
        db.session.add(obs)
        db.session.commit()
        return obs

    @staticmethod
    def get_observation_by_id(obs_id):
        return VitalObservation.query.get(obs_id)

    @staticmethod
    def list_by_document_id(doc_id):
        return VitalObservation.query.filter_by(document_id=doc_id).all()

    @staticmethod
    def associate_observation_to_document(obs_id, document_id):
        obs = VitalObservation.query.get(obs_id)
        if not obs:
            return None
        obs.document_id = document_id
        db.session.commit()
        return obs