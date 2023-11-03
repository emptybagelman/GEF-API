from flask import Blueprint
from flask import jsonify, request
from werkzeug import exceptions
from application import db
from application.blueprints.questions.model import Questions
import random

questions_bp = Blueprint("questions",__name__)

@questions_bp.route("/questions/<int:id>", methods=["GET"])
def get_by_id(id):
    try:
        question = Questions.query.filter_by(id=id).one()
    except:
        raise exceptions.NotFound("Question doesn't exist.")
    if request.method == "GET":
        return jsonify({"data":question.json}), 200   



@questions_bp.route("/questions/<string:difficulty>",methods=["GET"])
def get_all_by_difficulty(difficulty):
    if request.method == "GET":
        try:
            questions = Questions.query.filter_by(difficulty=difficulty).all()
            data = [r.json for r in questions]
            return jsonify({"questions":data})
        except:
            raise exceptions.InternalServerError("Dead, no work")



@questions_bp.route("/questions/random/<string:difficulty>",methods=["GET"])
def get_random_by_difficulty(difficulty):
    if request.method == "GET":
        try:
            questions = Questions.query.filter_by(difficulty=difficulty).all()
            print(f"{random.choice(questions)}\n\n\n")
            return jsonify({"questions":random.choice(questions).json})
        except Exception as e:
            raise e

@questions_bp.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"error": f"{err}"}), 404


@questions_bp.errorhandler(exceptions.InternalServerError)
def handle_500(err):
     return jsonify({"error": f"{err}"}), 500