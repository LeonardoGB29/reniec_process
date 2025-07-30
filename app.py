from flask import Flask
from extensions import db, migrate
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///dev.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "123456")

db.init_app(app)
migrate.init_app(app, db)

# Importa los modelos explícitamente para que Alembic los detecte
from domain.vital.model.Document import Document
from domain.vital.model.VitalCase import VitalCase

# Registro de blueprints
from presentation.vital.DocumentController import document_bp
from presentation.vital.ObservationController import observation_bp
from presentation.vital.VitalCaseController import vital_case_bp

app.register_blueprint(document_bp, url_prefix="/register_vital")
app.register_blueprint(observation_bp, url_prefix="/register_vital")
app.register_blueprint(vital_case_bp, url_prefix="/register_vital")

if __name__ == "__main__":
    app.run(debug=True)