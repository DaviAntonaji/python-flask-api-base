from resources.site import Site, Sites


class SiteRoutes:

    def __init__(self, api):
        self.api = api
        self.makeRoutes()
    
    def makeRoutes(self):
        self.api.add_resource(Sites, '/sites')
        self.api.add_resource(Site, '/sites/<string:url>')
