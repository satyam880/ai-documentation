# view.py
from flask import jsonify, Blueprint

# Create a Blueprint instead of a Flask app
bp = Blueprint('api', __name__)

@bp.route('/hello')
def hello():
    return jsonify({"message": "Hello, World!"})