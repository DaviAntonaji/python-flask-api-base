from flask_restful import reqparse, Resource
from auth import managertk
from flask_jwt_extended import jwt_required, get_jwt_identity
import json
from utils.S3FileManagement import S3FileManagement
from werkzeug.datastructures import FileStorage

atributos = reqparse.RequestParser()
atributos.add_argument(
    'file', type=FileStorage, location='files')


class EnviarArquivo(Resource):

    @jwt_required
    def post(self):

        dados = atributos.parse_args()

        file = dados['file']

        if file == None:
            return {"message": "Envie o arquivo como 'file'"}, 400

        arquivoNoS3 = S3FileManagement().sendFile(file, "uploads")

        return {
            "message": "OK",
            "file_path": arquivoNoS3
        }, 200
        
