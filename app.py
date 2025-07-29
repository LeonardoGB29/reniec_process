from flask import Flask
from extensions import db, migrate
from domain.vital.model.vital_case import VitalCase
import os
from dotenv import load_dotenv

REGISTER_VITAL_PREFIX = "/register_vital"

from presentation.vital.vital_case_controller import vital_case_bp

# Registrar los blueprints con el mismo prefijo
app.register_blueprint(document_bp, url_prefix=REGISTER_VITAL_PREFIX)
app.register_blueprint(observation_bp, url_prefix=REGISTER_VITAL_PREFIX)
app.register_blueprint(vital_case_bp, url_prefix=REGISTER_VITAL_PREFIX)

if __name__ == "__main__":
    app.run(debug=True)


load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///dev.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "123456")

db.init_app(app)
migrate.init_app(app, db)

from presentation.vital.document_controller import document_bp
from presentation.vital.observation_controller import observation_bp

#Esto es lo que le dice a Flask: escucha las rutas que empiecen con /register_vital.


from presentation.vital.vital_case_controller import vital_case_bp

app.register_blueprint(document_bp, url_prefix=REGISTER_VITAL_PREFIX)
app.register_blueprint(observation_bp, url_prefix=REGISTER_VITAL_PREFIX)

#Esto es lo que le dice a Flask: escucha las rutas que empiecen con /register_vital.

app.register_blueprint(vital_case_bp, url_prefix=REGISTER_VITAL_PREFIX)


if __name__ == "__main__":
    app.run(debug=True)
