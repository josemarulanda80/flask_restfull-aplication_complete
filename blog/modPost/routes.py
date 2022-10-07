
from flask_restful import Resource
from flask import (json,request)
import sqlalchemy
from blog.database import Post,User
from blog.common.utils.auth import RoleSchema, UserSchema
from werkzeug.security import generate_password_hash,check_password_hash
import jwt,json
from marshmallow import ValidationError
from blog import db
import datetime
from blog import app
from blog.common.utils.blog import PostPutSchema, PostSchema
from blog.common.utils.Schema_global import IdSchema

post_schema=PostSchema()
id_schema=IdSchema()
post_put_schema=PostPutSchema()
class PostBlog(Resource):
    """Clase para obtener todos los get existentes"""

    def get(self):
        posts=Post.query.all()
        
        if posts != None:      
            return {"post":[{"id":i.id,"title":i.title,"body":i.body}for i in posts]},200
        else:
            return {"message":"Not found"}
    
    def post(self):
        try:
            post=post_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 422
        except TypeError:
            return {"message":"bad request"},400
        user_name= User.query.filter_by(id = post.author).first()
        if user_name == None:
            return {"message":"Usuario no existe"},404
        db.session.add(post)
        db.session.commit()
        return {"post_id":post.id},201

    def delete(self):
        data=id_schema.load(request.args)
        post = Post.query.filter_by(id=data["id"]).first()
        if post!=None:
            db.session.delete(post)
            db.session.commit()
            return "",204
        else:
            return {"message":"Not found"},404
    
    def put(self):
        try:
         data = post_put_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 422
        except TypeError:
            return {"message":"Bad request"},400
     
        post= Post.query.filter_by(id=data["id"]).first()
        if post != None:
            post.title=data["title"]
            post.body=data["body"]
            db.session.commit()
            return {"message":"Post actualizado correctamente"},200
        else:
            {"Not Found"},404

class BlogUser(Resource):
    def get(self,id_user):
       
        all = Post.query.filter_by(author=id_user)
        user = User.query.filter_by(id=id_user).first()
        if user == None:
            return {"message":"Not Found"},404
        else:
            return {"username":user.username,"post":[{"title":i.title,"body":i.body,"id":i.id}for i in all]},200


class UniqueBlog(Resource):
#     data = json.loads(request.data)
    def get(self,id_blog):
        
        post = Post.query.filter_by(id=id_blog).first()
        if post!=None:
            return {"title":post.title,"body":post.body,"id":post.id},200
        else:
            return {"message":"Not Found"},404