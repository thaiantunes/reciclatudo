from flask import Flask
from routes.parceiro_routes import parceiro_blueprint
from routes.morador_routes import morador_blueprint
from routes.parceiro_routes import parceiro_blueprint
from routes.coletas_routes import coletas_blueprint

app = Flask(__name__)

app.register_blueprint(parceiro_blueprint)
app.register_blueprint(morador_blueprint)
app.register_blueprint(parceiro_blueprint)
app.register_blueprint(coletas_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
