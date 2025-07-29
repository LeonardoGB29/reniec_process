from flask import Flask
from extensions import db, migrate
#from controllers.document_controller import document_bp
from domain.vital.model.VitalCase import VitalCase
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///dev.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "123456")

db.init_app(app)
migrate.init_app(app, db)

from presentation.vital.document_controller import document_bp
from presentation.vital.ObservationController import observation_bp

#Esto es lo que le dice a Flask: escucha las rutas que empiecen con /register_vital.


from presentation.vital.VitalCaseController import vital_case_bp

app.register_blueprint(document_bp, url_prefix="/register_vital")
app.register_blueprint(observation_bp, url_prefix="/register_vital")

#Esto es lo que le dice a Flask: escucha las rutas que empiecen con /register_vital.

app.register_blueprint(vital_case_bp, url_prefix="/register_vital")


if __name__ == "__main__":
    app.run(debug=True)
