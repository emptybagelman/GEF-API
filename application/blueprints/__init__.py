from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object('config.Config')
    app.json_provider_class.sort_keys = False
    CORS(app)

    @app.route("/")
    def greet():
        return jsonify({
            "message":"Welcome to GeoKnight Reforged's API",
            "description":"Started: 03/11/23",
            "endpoint": [
                "GET /"
            ]
        }), 200
    
    db.init_app(app)

    with app.app_context():
        from application.blueprints.questions.questions import questions_bp

        app.register_blueprint(questions_bp)

        db.create_all()
        return app