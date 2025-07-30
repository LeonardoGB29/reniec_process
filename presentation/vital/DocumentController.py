from flask import Blueprint, request, jsonify
from application.vital.DocumentService import DocumentService
from application.vital.ObservationService import ObservationService
from application.vital.ActaService import ActaService
from application.vital.ValidationService import ValidationService
from infrastructure.vital.SqlAlchemyDocumentRepository import SqlAlchemyDocumentRepository

document_bp = Blueprint('document', __name__, url_prefix='/register_vital')
service = DocumentService(SqlAlchemyDocumentRepository())


# Crear documento (ajustado para solicitudRegistro)
@document_bp.route("/create_document", methods=["POST"])
def create_document():
    try:
        data = request.get_json()
        print(f"Received data: {data}")  # Depuración
        solicitud = data.get("solicitudRegistro")
        if not solicitud or not solicitud.get("number") or not solicitud.get("typeRegistro"):
            return jsonify({"error": "solicitudRegistro with number and typeRegistro is required"}), 400
        
        doc_data = {
            "number": solicitud["number"],
            "doc_type": solicitud["typeRegistro"],
            "case_id": solicitud.get("id"),
            "status": solicitud.get("estado", "PENDING")
        }
        print(f"Processed doc_data: {doc_data}")  # Depuración
        doc = service.register(doc_data)
        return jsonify({
            "ok": True,
            "id": doc.id,
            "number": doc.number,
            "doc_type": doc.doc_type,
            "status": doc.status
        }), 201
    except KeyError as e:
        print(f"KeyError: {e}")  # Depuración
        return jsonify({"error": f"Missing field in solicitudRegistro: {e}"}), 400
    except Exception as e:
        print(f"Exception occurred: {e}")  # Depuración
        return jsonify({"error": str(e)}), 500
    
# Listar documentos
@document_bp.route("/list_documents", methods=["GET"])
def list_documents():
    docs = service.list()
    return jsonify([
        {
            "id": d.id,
            "number": d.number,
            "type": d.doc_type,
            "status": d.status
        } for d in docs
    ])

# Obtener documento por ID
@document_bp.route("/get_document/<int:doc_id>", methods=["GET"])
def get_document(doc_id):
    doc = service.get(doc_id)
    if not doc:
        return jsonify({"error": "Document not found"}), 404
    return jsonify({
        "id": doc.id,
        "number": doc.number,
        "type": doc.doc_type,
        "status": doc.status
    })

# Actualizar estado del documento
@document_bp.route("/update_status/<int:doc_id>", methods=["PUT"])
def update_status(doc_id):
    data = request.get_json()
    if "status" not in data:
        return jsonify({"error": "Missing status field"}), 400

    try:
        doc = service.change_status(doc_id, data["status"])
        return jsonify({
            "id": doc.id,
            "status": doc.status
        })
    except ValueError:
        return jsonify({"error": "Document not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Asociar documento a persona
@document_bp.route('/associate_document_to_person/<int:doc_id>', methods=['PUT'])
def associate_document_to_person(doc_id):
    data = request.get_json()
    person_id = data.get("person_id")
    if not person_id:
        return jsonify({"error": "person_id is required"}), 400
    try:
        doc = service.associate_to_person(doc_id, person_id)
        return jsonify({
            "id": doc.id,
            "person_id": doc.person_id,
            "doc_type": doc.doc_type
        }), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

# Registrar observación
@document_bp.route('/create_observation', methods=['POST'])
def create_observation():
    data = request.get_json()
    solicitud = data.get("solicitudRegistro")
    if not solicitud or not solicitud.get("document_id") or not solicitud.get("observaciones"):
        return jsonify({"error": "solicitudRegistro with document_id and observaciones is required"}), 400
    try:
        observation = ObservationService().create(solicitud["document_id"], solicitud["observaciones"])
        return jsonify({
            "ok": True,
            "id": observation.id,
            "document_id": observation.document_id,
            "description": observation.description,
            "created_at": observation.created_at.isoformat(),
            "status": observation.status
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 500

# Registrar acta
@document_bp.route('/create_acta', methods=['POST'])
def create_acta():
    data = request.get_json()
    solicitud = data.get("solicitudRegistro")
    if not solicitud or not solicitud.get("document_id") or not solicitud.get("actaTexto"):
        return jsonify({"error": "solicitudRegistro with document_id and actaTexto is required"}), 400
    try:
        acta = ActaService().create(solicitud["document_id"], solicitud["actaTexto"])
        return jsonify({
            "ok": True,
            "id": acta.id,
            "document_id": acta.document_id,
            "acta_texto": acta.acta_texto,
            "created_at": acta.created_at.isoformat(),
            "status": acta.status
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 500

# Validar requisitos
@document_bp.route('/validate_requirements', methods=['POST'])
def validate_requirements():
    data = request.get_json()
    solicitud = data.get("solicitudRegistro")
    if not solicitud or not solicitud.get("id"):
        return jsonify({"error": "solicitudRegistro with id is required"}), 400
    try:
        is_valid, message = ValidationService().validate_requirements(solicitud["id"])
        return jsonify({
            "ok": is_valid,
            "message": message
        }), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 500
