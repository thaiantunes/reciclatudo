from flask import Blueprint, request, jsonify
from models import Morador
from models.database import db_session

morador_blueprint = Blueprint('morador_blueprint', __name__)

@morador_blueprint.route('/morador/', methods=['POST'])
def create_morador():
    data = request.get_json()

    new_morador = Morador(
        nome=data['nome'],
        cep=data['cep'],
        logradouro=data['logradouro'],
        bairro=data['bairro'],
        ddd=data['ddd'],
        telefone=data['telefone'],
        email=data['email']
    )
    with db_session() as session:
        session.add(new_morador)
        session.commit()

    return jsonify({"message": "Morador criado com sucesso!"}), 201

