from flask_restful import Resource, reqparse

class Library(Resource):

    def get(self):
        return { 'test': 1 }

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass