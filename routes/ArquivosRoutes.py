from resources.uploads import EnviarArquivo

class ArquivosRoutes:

    def __init__(self, api):
        self.api = api
        self.makeRoutes()
    
    def makeRoutes(self):
        self.api.add_resource(EnviarArquivo, '/files/upload')