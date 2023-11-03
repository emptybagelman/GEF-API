from flask import Blueprint
from flask import jsonify, request
from werkzeug import exceptions
from application import db
from application.blueprints.questions.model import Questions

questions_bp = Blueprint("questions",__name__)

@questions_bp.route("/questions/<int:id>", methods=["GET"])
def get_question(id):
    try:
        question = Questions.query.filter_by(id=id).one()
    except:
        raise exceptions.NotFound("Question doesn't exist.")
    if request.method == "GET":
        return jsonify({"data":user.json}), 200
    


@users_bp.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"error": f"{err}"}), 404


@users_bp.errorhandler(exceptions.InternalServerError)
def handle_500(err):
     return jsonify({"error": f"{err}"}), 500

