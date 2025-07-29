from flask import Flask
from extensions import db, migrate
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///dev.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "123456")

db.init_app(app)
migrate.init_app(app, db)

REGISTER_VITAL_PREFIX = "/register_vital"

from presentation.vital.document_controller import document_bp
from presentation.vital.observation_controller import observation_bp
from presentation.vital.vital_case_controller import vital_case_bp

app.register_blueprint(document_bp, url_prefix=REGISTER_VITAL_PREFIX)
app.register_blueprint(observation_bp, url_prefix=REGISTER_VITAL_PREFIX)
app.register_blueprint(vital_case_bp, url_prefix=REGISTER_VITAL_PREFIX)


if __name__ == "__main__":
    app.run(debug=True)
