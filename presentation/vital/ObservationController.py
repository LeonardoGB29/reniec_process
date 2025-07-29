from flask import Blueprint, request, jsonify
from application.vital.ObservationService import ObservationService


observation_bp = Blueprint('vital_observation', __name__, url_prefix='/register_vital')

@observation_bp.route('/create_observation', methods=['POST'])
def create_observation():
    data = request.get_json()
    obs = ObservationService.create_observation(data)
    return jsonify({
        "success": True,
        "data": {
            "id": obs.id,
            "title": obs.title,
            "description": obs.description,
            "document_id": obs.document_id,
            "observed_at": obs.observed_at
        }
    }), 201

@observation_bp.route('/get_observation/<int:obs_id>', methods=['GET'])
def get_observation(obs_id):
    obs = ObservationService.get_observation_by_id(obs_id)
    if obs is None:
        return jsonify({"success": False, "error": "Observation not found"}), 404
    return jsonify({
        "success": True,
        "data": {
            "id": obs.id,
            "title": obs.title,
            "description": obs.description,
            "document_id": obs.document_id,
            "observed_at": obs.observed_at
        }
    })

@observation_bp.route('/list_observations/<string:doc_id>', methods=['GET'])
def list_by_document(doc_id):
    observations = ObservationService.list_by_document_id(doc_id)
    return jsonify({
        "success": True,
        "data": [
            {
                "id": obs.id,
                "title": obs.title,
                "description": obs.description,
                "document_id": obs.document_id,
                "observed_at": obs.observed_at
            } for obs in observations
        ]
    })

@observation_bp.route('/associate_observation_to_document', methods=['PUT'])
def associate_to_document():
    data = request.get_json()
    obs_id = data.get("observation_id")
    document_id = data.get("document_id")
    obs = ObservationService.associate_observation_to_document(obs_id, document_id)
    if obs is None:
        return jsonify({"success": False, "error": "Observation not found"}), 404
    return jsonify({
        "success": True,
        "data": {
            "id": obs.id,
            "title": obs.title,
            "description": obs.description,
            "document_id": obs.document_id,
            "observed_at": obs.observed_at
        }
    })
