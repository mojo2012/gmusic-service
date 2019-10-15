from flask import Flask
from flask_restful import Api, Resource, Resource
#from . import webapp
from .rest.library import Library
from .rest.authentication import Authentication

print('Starting gmusic-service')

app = Flask(__name__)
api = Api(app)

api.add_resource(Authentication, "/auth/")
api.add_resource(Library, "/library/")

app.run(debug=True)