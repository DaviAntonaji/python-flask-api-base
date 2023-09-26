from models.UserModel import UserModel
from database.connection import connectionDb
from functions.uuid_manager import UUIDManager
class UserORM:

    def auth(email,password):
        conexao = connectionDb.connect()
        cursor = conexao.cursor()
        try:
            cursor.execute( "SELECT * FROM users WHERE user_email = %s AND user_password=md5(%s)", (email, password))
            user = cursor.fetchone()
            if user:
                print(user["user_status"])
                if user["user_status"] != 1:
                    return {"message": "Usuário desativado", "status_code": 400}        
                
                model = UserModel(user).json()
                return {"message": "OK", "user": model}
            return {"message": "User not found", "status_code": 404}

        except Exception as e:
            
            return {"message": "Requisição incorreta", "status_code": 400, "error": str(e)}
        finally:
            cursor.close()
            conexao.close()
    
    def getById(id):
        conexao = connectionDb.connect()
        cursor = conexao.cursor()
        try:
            cursor.execute( "SELECT * FROM users WHERE user_id = %s", (id))
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

    def getByEmail(email):
        conexao = connectionDb.connect()
        cursor = conexao.cursor()
        try:
            cursor.execute( "SELECT * FROM users WHERE user_email = %s", (email))
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

    
    def insert(user):
        conexao = connectionDb.connect()
        cursor = conexao.cursor()
        try:
            if UserORM.getByEmail(user["user_email"])["message"] == "OK":
                return {"message": "Usuário já cadastrado", "status_code": 400}
            user["user_id"] = UUIDManager.generate_uuid()
            cursor.execute( "INSERT INTO users VALUES (%s, %s, %s, md5(%s), %s)", (user["user_id"], user["user_name"], user["user_email"], user["user_password"], user["user_status"]))
            conexao.commit()
            return {"message": "OK", "user_id": user["user_id"]}

        except Exception as e:
            
            return {"message": "Requisição incorreta", "status_code": 400, "error": str(e)}
        finally:
            cursor.close()
            conexao.close()
    
    def listAll():
        conexao = connectionDb.connect()
        cursor = conexao.cursor()
        try:
            cursor.execute( "SELECT * FROM users")
            users = []
            for user in cursor.fetchall():
                model = UserModel(user).json()
                users.append(model)
            print(users)
            return {"message": "OK", "users": users}

        except Exception as e:
            
            return {"message": "Requisição incorreta", "status_code": 400, "error": str(e)}
        finally:
            cursor.close()
            conexao.close()