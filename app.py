from flask                                                  import Flask
from flask_cors 										    import CORS
from flask_restful                                          import Api  

from flask import jsonify,request
from flask_jwt_extended                                     import JWTManager

from resources.start                                        import Start

from resources.users                                        import GetUserByID,UserAuth
import os
from dotenv                                                 import load_dotenv
load_dotenv()


app = Flask(__name__) 

app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY") # Chave de autenticação JWT
CORS(app)



api = Api(app)

jwt =JWTManager(app)


@jwt.revoked_token_loader
def token_de_acesso_invalidado():
    return {'message': 'Você foi desconectado.'}, 401 # unauthorized


@app.route("/get_ip", methods=["GET"])

def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200


api.add_resource(Start, "/")

api.add_resource(GetUserByID, "/user/id/<string:user_id>")
api.add_resource(UserAuth, "/user/auth")


# Main Function 
if __name__ == '__main__':
    print("API PYTHON INICIADA")
    # sendSlackBot(":white_check_mark: API iniciada com sucesso!")
    app.run(host='0.0.0.0', port=5001, debug=True)
