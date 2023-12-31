from flask import Blueprint
from flask import jsonify, request
from werkzeug import exceptions
from application import db
from application.blueprints.scoreboard.model import Scoreboard

scoreboard_bp = Blueprint("scoreboard",__name__)

@scoreboard_bp.route("/scoreboard",methods=["GET","POST"])
def get_all():
    try:
        scoreboard = Scoreboard.query.all()
        data = [r.json for r in scoreboard]
    except:
        raise exceptions.InternalServerError("Dead, no work")
    
    if request.method == "GET":
        return jsonify({"data":data}), 200
    if request.method == "POST":
        try:

            data = request.get_json()

            username = data.get("username")
            score = data.get("score")

            new_score = Scoreboard(username=username,score=score)

            db.session.add(new_score)
            db.session.commit()

            return jsonify({"data": new_score.json}), 201
        
        except Exception as e:
            return f"An error occurred: {str(e)}", 400
    
@scoreboard_bp.route("/scoreboard/top/<int:amount>",methods=["GET"])
def get_top_x(amount):
    if request.method == "GET":
        top_values = Scoreboard.query.order_by(Scoreboard.score.desc()).limit(int(amount)).all()
        top_values = [item.json for item in top_values]
        return jsonify({"top_values":top_values})





@scoreboard_bp.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"error": f"{err}"}), 404


@scoreboard_bp.errorhandler(exceptions.InternalServerError)
def handle_500(err):
     return jsonify({"error": f"{err}"}), 500