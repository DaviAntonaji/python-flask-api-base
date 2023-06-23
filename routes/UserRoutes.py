from resources.usuario import User, UserRegister, UserLogin, UserLogout, UserConfirm

class UserRoutes:

    def __init__(self, api):
        self.api = api
        self.makeRoutes()
    
    def makeRoutes(self):
        self.api.add_resource(User, '/usuarios/<int:user_id>')
        self.api.add_resource(UserRegister, '/cadastro')
        self.api.add_resource(UserLogin, '/login')
        self.api.add_resource(UserLogout, '/logout')
        self.api.add_resource(UserConfirm, '/confirmacao/<int:user_id>')