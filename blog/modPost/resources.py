from flask import  Blueprint
from flask_restful import Api
from blog.modPost.routes import BlogUser, PostBlog, UniqueBlog


api_post = Blueprint('post',__name__,url_prefix='/posts')
api = Api(api_post)


api.add_resource(PostBlog,'')
api.add_resource(UniqueBlog,"/<int:id_blog>")
api.add_resource(BlogUser,'/user/<int:id_user>/posts')