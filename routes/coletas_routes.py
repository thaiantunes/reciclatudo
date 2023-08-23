from flask import Blueprint, jsonify
from models import Coleta
# from database import db

coletas_blueprint = Blueprint('coletas_routes', __name__)

@coletas_blueprint.route('/coletas/locais', methods=['GET'])
def get_coleta_locais():
    coletas = Coleta.query.all()
    return jsonify([{"latitude": coleta.latitude, "longitude": coleta.longitude, "descricao": coleta.descricao} for coleta in coletas])

