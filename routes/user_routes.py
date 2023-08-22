# routes/user_routes.py
from flask import Blueprint, request
user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/register', methods=['POST'])
def register():
    pass

@user_blueprint.route('/login', methods=['POST'])
def login():
    pass
