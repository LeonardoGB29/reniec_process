#!/usr/bin/python
#-*- coding: utf-8 -*-


from flask import Blueprint, request, jsonify
from application.vital.VitalCaseService import VitalCaseService

vital_case_bp = Blueprint("vital_case_bp", __name__)
service = VitalCaseService()

@vital_case_bp.route("/vital_cases", methods=["POST"])
def create_vital_case():
    data = request.get_json()
    case = service.create_case(data)
    return jsonify({
        "id": case.id,
        "status": case.status,
        "person_id": case.person_id
    }), 201

@vital_case_bp.route("/vital_cases", methods=["GET"])
def list_vital_cases():
    cases = service.list_cases()
    return jsonify([
        {"id": c.id, "status": c.status, "person_id": c.person_id}
        for c in cases
    ])

@vital_case_bp.route("/vital_cases/<int:case_id>", methods=["GET"])
def get_vital_case(case_id):
    case = service.get_case(case_id)
    if not case:
        return jsonify({"error": "Not found"}), 404
    return jsonify({
        "id": case.id,
        "status": case.status,
        "person_id": case.person_id
    })

@vital_case_bp.route("/vital_cases/<int:case_id>", methods=["PUT"])
def update_vital_case_status(case_id):
    data = request.get_json()
    new_status = data.get("status")
    case = service.update_status(case_id, new_status)
    if not case:
        return jsonify({"error": "Not found"}), 404
    return jsonify({
        "id": case.id,
        "status": case.status,
        "person_id": case.person_id
    })
