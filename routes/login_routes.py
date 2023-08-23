from flask import Blueprint
from flask import render_template, request, redirect, url_for, flash
import os

login_blueprint = Blueprint('login_blueprint', __name__)

@login_blueprint.route('/home')
def home():
    return "Welcome to the home page"

@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Here you should check the username and password against your user database
        # For simplicity, let's assume username: "admin" and password: "password"
        if username == 'admin' and password == 'password':
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Please check your credentials.', 'error')
    
    template_path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'login.html')

    return render_template(template_path)
