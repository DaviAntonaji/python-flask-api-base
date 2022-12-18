from flask_restful import reqparse, Resource
from auth import managertk
from flask_jwt_extended import jwt_required, get_jwt_identity
import json
from utils.S3FileManagement import S3FileManager

atributos = reqparse.RequestParser()
atributos.add_argument(
    'file', type=werkzeug.datastructures.FileStorage, location='files')


class EnviarArquivoParaPublicacao(Resource):

    @jwt_required
    def post(self):

        dados = atributos.parse_args()

        currentDataToken = managertk.decodedPayload(get_jwt_identity())
        currentDataToken = json.loads(currentDataToken)

        file = dados['file']

        if file == None:
            return {"message": "Envie o arquivo como 'file'"}, 400

        CaminhoParaArquivo = S3FileManager().SendFile(file, "ArquivoNome", f"user_posts/{usuarioLink}/")
        return {
            "message": "OK",
            "file_path": CaminhoParaArquivo
        }, 200
        
class RecuperaArquivoSemAutenticacacao(Resource):

    def get(self, ArquivoId):
        retornoArquivo = ArquivoModel.recuperarArquivo(ArquivoId)
        if retornoArquivo["message"] == "OK":
            
            retArquivo = retornoArquivo["arquivo"]
            if retArquivo["ArquivoObrigaAutenticacao"] != 0:
                return {"message": "Para visualizar este arquivo você precisa requisitar a rota de arquivos autenticados"}, 401
            Arquivo = GerenciamentoDeArquivosS3().RecuperarArquivoDoS3(retornoArquivo["arquivo"]["CaminhoParaArquivo"])
            return Response(
                    Arquivo['Body'].read(),
                    mimetype=retArquivo["ArquivoMimeType"],
                    headers={"Content-Disposition": "attachment;filename={}".format(retArquivo["ArquivoNome"])}
            )
            
        else:
            return retornoArquivo, retornoArquivo["status_code"]
