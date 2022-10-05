from flask import  Blueprint
from flask_restful import Api, Resource, url_for
from blog.mod.routes import AddRoles, Auth, Session, UpdateRoles

api_bp = Blueprint('api',__name__,url_prefix='/auth')
api = Api(api_bp)

api.add_resource(Auth, '/user')
api.add_resource(AddRoles,'/user/roles')
api.add_resource(UpdateRoles,'/user/roles/<int:id_rol>')
api.add_resource(Session, '/login')
