from flask import Blueprint, request, jsonify
from ...application.vital.document_service import DocumentService
from ...infrastructure.vital import SqlAlchemyDocumentRepository

document_bp = Blueprint("register_vital", __name__)
service = DocumentService(SqlAlchemyDocumentRepository())

@document_bp.route("/create_document", methods=["POST"])
def create_document():
    try:
        data = request.get_json()
        doc = service.register(data)
        return jsonify({
            "id": doc.id,
            "number": doc.number,
            "type": doc.doc_type,
            "status": doc.status
        }), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field: {e}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

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

