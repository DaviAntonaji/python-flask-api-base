from resources.hotel import Hoteis, Hotel

class HotelRoutes:

    def __init__(self, api):
        self.api = api
        self.makeRoutes()
    
    def makeRoutes(self):
        self.api.add_resource(Hoteis, '/hoteis')
        self.api.add_resource(Hotel, '/hoteis/<string:hotel_id>')