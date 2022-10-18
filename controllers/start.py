from flask_restful import reqparse, Resource
import json

class Start(Resource):
  
    def get(self):

      return {"name": "PYTHON FLASK API", "version": "1.0", "authors": "Davi Antonaji", "description": "Template API Flask"}, 200
