from controllers.UserController import GetUserByID,UserAuth

class UserRoutes():
    
    def __init__(self,api):
        self.api = api
        self.makeRoutes()
        
    def makeRoutes(self):
        self.api.add_resource(GetUserByID, "/user/id/<string:user_id>")
        self.api.add_resource(UserAuth, "/user/auth")