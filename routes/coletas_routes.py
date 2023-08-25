from flask import Blueprint, Flask, render_template, request
import requests
from models import Coleta
from models.database import db_session


coletas_blueprint = Blueprint('coletas_routes', __name__)

@coletas_blueprint.route('/endereco', methods=['GET'])
def search_address():
    return render_template('procura_endereco.html')


@coletas_blueprint.route('/coletas', methods=['GET'])
def show_map():
    address = request.args.get('address')

    if not address:
        return 'Address parameter missing', 400

    base_url = 'https://nominatim.openstreetmap.org/search'
    params = {
        'q': address,
        'format': 'json'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data:
        result = data[0]
        latitude = result['lat']
        longitude = result['lon']
        return render_template('recolhimento.html', latitude=latitude, longitude=longitude)
    else:
        return 'Geocoding failed', 500



# # Rota para obter todos os locais de coleta
# @coletas_blueprint.route('/coletas/locais', methods=['GET'])
# def get_coleta_locais():
#     coletas = Coleta.query.all()
#     return jsonify([{"id_coleta": coleta.id_coleta, "latitude": coleta.latitude, "longitude": coleta.longitude, "data": coleta.data, "turno": coleta.turno, "quantidade": coleta.quantidade} for coleta in coletas])

# # Rota para adicionar uma nova coleta
# @coletas_blueprint.route('/coletas/add', methods=['POST'])
# def add_coleta():
#     data = request.json
#     nova_coleta = Coleta(
#         latitude = data['latitude'],
#         longitude = data['longitude'],
#         data = data['data'],
#         turno = data['turno'],
#         quantidade = data['quantidade']
#     )
    
#     db_session.add(nova_coleta)
#     db_session.commit()
    
#     return jsonify({"message": "Coleta adicionada com sucesso!"}), 201
