from flask import  Blueprint
from flask_restful import Api
from blog.modFile.routes import l
from blog.modPost.routes import BlogUser, PostBlog, UniqueBlog


api_file = Blueprint('file',__name__,url_prefix='/files')
api = Api(api_file)

api.add_resource(l,'')