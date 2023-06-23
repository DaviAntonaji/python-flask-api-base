from flask_restful import Resource


class _Start(Resource):
    def get(self):
        return {
            "title": "API Base Project",
            "description": "Um projeto base para criar APIs utilizando Python.",
            "author": "Davi Antonaji",
            "version": "1.0.0",
            "github_repository": "https://github.com/DaviAntonaji/python-flask-api-base"
        }, 200


class StartRoute:

    def __init__(self, api):
        self.api = api
        self.makeRoutes()

    def makeRoutes(self):
        self.api.add_resource(_Start, '/')
