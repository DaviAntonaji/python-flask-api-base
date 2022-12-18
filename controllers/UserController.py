from flask_restful import reqparse, Resource
from auth import managertk
from app.User import User
from flask_jwt_extended import jwt_required, get_jwt_identity
import json

atributosLogin = reqparse.RequestParser()
atributosLogin.add_argument('email', required=True, help="The field email cannot be left blank.")
atributosLogin.add_argument('password', required=True, help="The field password  cannot be left blank.")

class UserAuth(Resource):

    def post(self):
        dados = atributosLogin.parse_args()
        user = UserModel.auth(dados['email'], dados['password'])

        if user:
            if user["message"] == "OK":
                if int(user["user_status"]) != 1:
                    return {"message": "Usuario incorreto"},400
                token_de_acesso = managertk.createToken(json.dumps(user))
                return {'message': 'OK','token': token_de_acesso, 'user' :user}, 200
            else:
                return user, user["status_code"]
        return {"message":"E-mail ou senhas incorretos"}, 400
    
    

class GetUserByID(Resource):
    
    @jwt_required
    def get(self, user_id):
        
        user = UserModel.getUserById(user_id)
        freshAccessToken = managertk.createFreshToken()
        user.update({"refreshToken": freshAccessToken})

        if user["message"] == "OK":
            return user,200
        else:
            return user, user["status_code"]