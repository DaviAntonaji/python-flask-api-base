from tokenpass import managertk
from database.connection import connectionDb

class UserModel(object):
    
    def __init__(self, obj):

        self.user_id = obj[0]
        self.user_name = obj[1]
        self.user_email = obj[2]
        self.user_password = str(obj[3])
        self.user_status = obj[4]
        
    def json(self):
        return {
            "user_id": managertk.encodedPayload(str(self.user_id)),
            "user_name": self.user_name,
            "user_email": self.user_email,
            "user_password": self.user_password,
            "user_status": self.user_status
        }

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
            
            
            