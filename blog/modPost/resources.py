from flask import  Blueprint
from flask_restful import Api
from blog.modUser.routes import AddRoles, Auth, Session, UpdateRoles


api_post = Blueprint('post',__name__,url_prefix='/post')
api = Api(api_post)