from controllers.UserController import Auth, GetByID, ListAll, Insert

class UserRoutes:

    def __init__(self, api):
        self.api = api
        self.makeRoutes()
    
    def makeRoutes(self):
        self.api.add_resource(ListAll, '/usuarios')
        self.api.add_resource(Insert, '/register')
        self.api.add_resource(GetByID, '/usuarios/<string:user_id>')
        self.api.add_resource(Auth, '/login')