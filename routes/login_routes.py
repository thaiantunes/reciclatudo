from flask import Blueprint
from flask import render_template, request, redirect, url_for, flash


login_blueprint = Blueprint('login_blueprint', __name__)

@login_blueprint.route('/')
def index():
    return "Welcome to the root page"

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
        if username == 'admin' and password == 'admin':
            flash('Login successful', 'success')
            return redirect(url_for('login_blueprint.home'))
        else:
            flash('Login failed. Please check your credentials.', 'error')
    
    return render_template('login.html')
