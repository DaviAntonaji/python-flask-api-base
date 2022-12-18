class UserModel(object):
    
    def __init__(self, obj):

        self.user_id = obj[0]
        self.user_name = obj[1]
        self.user_email = obj[2]
        self.user_status = obj[3]
        
    def json(self):
        return {
            "user_id": managertk.encodedPayload(str(self.user_id)),
            "user_name": self.user_name,
            "user_email": self.user_email,
            "user_status": self.user_status
        }

    
            
            