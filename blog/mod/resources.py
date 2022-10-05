from flask import  Blueprint
from flask_restful import Api, Resource, url_for
from blog.mod.routes import Auth, Session, TodoItem

api_bp = Blueprint('api',__name__,url_prefix='/auth')
api = Api(api_bp)

api.add_resource(TodoItem, '/auth/<int:id>')
api.add_resource(Auth, '/register')
api.add_resource(Session, '/login')