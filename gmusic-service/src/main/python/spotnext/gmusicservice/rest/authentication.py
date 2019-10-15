from flask_restful import Resource, reqparse
from flask import request

class Authentication(Resource):

    def post(self):
        data = request.data
        
        return {
            'token': 'a'
        }

    def delete(self):
        pass