

class UserModel:
    def __init__(self, obj):
        # Coloque o tipo BINARY(36) no banco de dados, sem auto increment
        self.user_id = obj["user_id"].decode('utf-8')
        self.user_name = obj["user_name"]
        self.user_email = obj["user_email"]
        self.user_password = obj["user_password"]
        self.user_status = obj["user_status"]
        
    def json(self):
        return {
            "user_id": self.user_id,
            "user_name": self.user_name,
            "user_email": self.user_email,
            "user_status": self.user_status
        }
