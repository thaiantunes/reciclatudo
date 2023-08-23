# routes/user_routes.py
from flask import Blueprint
from flask import render_template, request, redirect, url_for, flash
import os

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/register', methods=['POST'])
def register():
    pass
