from flask_restful import Resource

class TodoItem(Resource):
    def get(self, id):
        return {'task': 'Say "Hello, World!"'}