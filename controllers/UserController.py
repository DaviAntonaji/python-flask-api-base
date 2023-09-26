from flask_restful import reqparse, Resource
from auth import managertk
from flask_jwt_extended import jwt_required, get_jwt_identity
import json
from orm.UserORM import UserORM

atributosLogin = reqparse.RequestParser()
atributosLogin.add_argument('email', required=True, help="The field email cannot be left blank.")
atributosLogin.add_argument('password', required=True, help="The field password  cannot be left blank.")

class Auth(Resource):

    def post(self):
        dados = atributosLogin.parse_args()
        user = UserORM.auth(dados['email'], dados['password'])

        if user:
            if user["message"] == "OK":
                token_de_acesso = managertk.createToken(json.dumps(user["user"]["user_id"]))
                return {'message': 'OK','token': token_de_acesso, 'user' :user}, 200
            else:
                return user, user["status_code"]
        return {"message":"E-mail ou senhas incorretos"}, 400
    
    

class GetByID(Resource):
    
    @jwt_required()
    def get(self, user_id):
        
        user = UserORM.getById(user_id)


        if user["message"] == "OK":
            return user,200
        else:
            return user, user["status_code"]
        
class ListAll(Resource):
    
    @jwt_required()
    def get(self):
        user = UserORM.listAll()
        freshAccessToken = managertk.createFreshToken()
        user.update({"refreshToken": freshAccessToken})
        if user["message"] == "OK":
            return user,200
        else:
            return user, user["status_code"]
        


atributos = reqparse.RequestParser()
atributos.add_argument('user_name', required=True, help="The field user_name cannot be left blank.")
atributos.add_argument('user_email', required=True, help="The field user_email cannot be left blank.")
atributos.add_argument('user_password', required=True, help="The field user_password  cannot be left blank.")
atributos.add_argument('user_status', required=True, help="The field user_status  cannot be left blank.")

class Insert(Resource):

    def post(self):
        dados = atributos.parse_args()
        user = UserORM.insert(dados)

        if user:
            if user["message"] == "OK":
                return user, 200
            else:
                return user, user["status_code"]
        return {"message":"E-mail ou senhas incorretos"}, 400