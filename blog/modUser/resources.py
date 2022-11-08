from flask import  Blueprint
from flask_restful import Api
from blog.modUser.routes import AddRoles, Auth, Session, UpdateRoles

api_bp = Blueprint('api',__name__,url_prefix='/auth')
api = Api(api_bp)

#Definición de las rutas y las clases 
api.add_resource(Auth, '/users')
api.add_resource(AddRoles,'/users/roles')
api.add_resource(UpdateRoles,'/users/roles/<int:id_rol>')
api.add_resource(Session, '/login')
