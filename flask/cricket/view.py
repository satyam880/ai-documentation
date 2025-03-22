# cricket/view.py
from flask import jsonify, Blueprint

# Create a Blueprint for the cricket app
bp_cricket = Blueprint('cricket', __name__)

@bp_cricket.route('/cricket/score')
def cricket_score():
    return jsonify({"message": "This is the cricket score!"})

@bp_cricket.route('/cricket/players')
def cricket_players():
    return jsonify({"message": "This is the list of cricket players!"})