from flask import Blueprint, jsonify, request
from models import Coleta
from database import db

coletas_blueprint = Blueprint('coletas_routes', __name__)

# Rota para obter todos os locais de coleta
@coletas_blueprint.route('/coletas/locais', methods=['GET'])
def get_coleta_locais():
    coletas = Coleta.query.all()
    return jsonify([{"id_coleta": coleta.id_coleta, "latitude": coleta.latitude, "longitude": coleta.longitude, "data": coleta.data, "turno": coleta.turno, "quantidade": coleta.quantidade} for coleta in coletas])

# Rota para adicionar uma nova coleta
@coletas_blueprint.route('/coletas/add', methods=['POST'])
def add_coleta():
    data = request.json
    nova_coleta = Coleta(
        latitude = data['latitude'],
        longitude = data['longitude'],
        data = data['data'],
        turno = data['turno'],
        quantidade = data['quantidade']
    )
    
    db.session.add(nova_coleta)
    db.session.commit()
    
    return jsonify({"message": "Coleta adicionada com sucesso!"}), 201
