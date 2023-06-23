from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST
import os
from dotenv import load_dotenv
from flask_cors import CORS
load_dotenv()

from routes.HotelRoutes import HotelRoutes
from routes.SiteRoutes import SiteRoutes
from routes.UserRoutes import UserRoutes
from routes.StartRoute import StartRoute


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
app.config['JWT_BLACKLIST_ENABLED'] = True
CORS(app)
api = Api(app)
jwt = JWTManager(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

@jwt.token_in_blocklist_loader
def verifica_blacklist(token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado():
    return jsonify({'message': 'You have been logged out.'}), 401 # unauthorized

HotelRoutes(api)
SiteRoutes(api)
UserRoutes(api)
StartRoute(api)

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(port=int(os.getenv("APPLICATION_PORT")), debug=True)
