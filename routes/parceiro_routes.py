from flask import Blueprint, request, jsonify
from models.data_model import Parceiro
from models.database import db_session


parceiro_blueprint = Blueprint('parceiro_blueprint', __name__)

@parceiro_blueprint.route('/parceiro/', methods=['POST'])
def create_parceiro():
    data = request.get_json()

    new_parceiro = Parceiro(
        nome_instituicao=data['nome_instituicao'],
        responsavel=data['responsavel'],
        cep=data['cep'],
        logradouro=data['logradouro'],
        bairro=data['bairro'],
        ddd=data['ddd'],
        telefone=data['telefone'],
        email=data['email']
    )

    with db_session() as session:
        session.add(new_parceiro)
        session.commit()

    return jsonify({"message": "Parceiro criado com sucesso!"}), 201

