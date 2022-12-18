from auth import managertk
from database.connection import connectionDb
from models.UserModel import UserModel

class User:
    
    @staticmethod
    def getUserById(user_id):
        conexao = connectionDb.connect()
        cursor = conexao.cursor()
        try:
            cursor.execute( "SELECT * FROM users WHERE user_id = %s", (managertk.decodedPayload(user_id)))
            user = cursor.fetchone()
            if user:
                model = UserModel(user).json()
                return {"message": "OK", "user": model}
            return {"message": "User not found", "status_code": 404}

        except Exception as e:
            
            return {"message": "Requisição incorreta", "status_code": 400, "error": str(e)}
        finally:
            cursor.close()
            conexao.close()
    
    @staticmethod
    def auth(email,senha):
        conexao = connectionDb.connect()
        cursor = conexao.cursor()
        try:
            
            cursor.execute( "SELECT * FROM users WHERE user_email = %s AND user_senha=md5(%s)", (email, senha))
            user = cursor.fetchone()
            if user:
                model = UserModel(user).json()

                return {"message": "OK", "user": model}
            return {"message": "User not found", "status_code": 404}

        except Exception as e:
            
            return {"message": "Requisição incorreta", "status_code": 400, "error": str(e)}

        finally:
            cursor.close()
            conexao.close()
            
    