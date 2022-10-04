from flask_restful import Resource
from flask import (json,request)
from blog.data_base import User

class TodoItem(Resource):
    def get(self, id):
        return {'task': 'Say "Hello, World!"'}


class Auth(Resource):
    def post(self):
        data = json.loads(request.data)
        print(data)
        return{"Recibido":data}
