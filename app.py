from flask import Flask, jsonify,request
from flask_restful import Api
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST
import os
from dotenv import load_dotenv
from flask_cors import CORS

from routes.UserRoutes import UserRoutes
from routes.StartRoute import StartRoute

load_dotenv()

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
app.config['JWT_BLACKLIST_ENABLED'] = True
# app.config['JWT_IDENTITY_CLAIM'] = 'jti' 

CORS(app)
api = Api(app)
jwt = JWTManager(app)

@app.route("/get_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200




@jwt.token_in_blocklist_loader
def verifica_blocklist(token, jwt_payload):
    jti = jwt_payload["jti"]
    return jti in BLACKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado(token, jwt_payload):
    return jsonify({'message': 'You have been logged out.'}), 401


UserRoutes(api)
StartRoute(api)


if __name__ == '__main__':
    app.run(port=int(os.getenv("APPLICATION_PORT")), debug=True)
