from msilib.schema import File
from flask import  Blueprint
from flask_restful import Api
from blog.modFile.routes import FileUserDownload, FileUrl, FileUserPostPut, UserImg
from blog.modPost.routes import BlogUser, PostBlog, UniqueBlog


api_file = Blueprint('file',__name__,url_prefix='/files')
api = Api(api_file)

api.add_resource(FileUrl,'/<string:name_file>')
api.add_resource(FileUserDownload,'/downloads/<string:name_file>')
api.add_resource(FileUserPostPut,'/users/<int:id>')
api.add_resource(UserImg,'/users/<int:id>/img')