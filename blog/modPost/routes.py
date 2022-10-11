
from flask_restful import Resource
from flask import (request)
from blog.database import Post,User
from marshmallow import ValidationError
from blog import db
from blog.common.utils.blog import PostPutSchema, PostSchema
from blog.common.utils.Schema_global import IdSchema

post_schema=PostSchema()
id_schema=IdSchema()
post_put_schema=PostPutSchema()
class PostBlog(Resource):
    """Clase para obtener todos los get existentes"""

    def get(self):
        posts=Post.query.all()
        return {"post":[{"id":i.id,"title":i.title,"body":i.body}for i in posts]},200
    
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
        try:
            data=id_schema.load(request.args)
        except ValidationError as err:
            return err.messages, 422
       
        post = Post.query.filter_by(id=data["id"]).first()
        if post!=None:
            db.session.delete(post)
            db.session.commit()
            return "",204
        else:
            return {"message":"Not found"},404
    
    def put(self):
        try:
            data=post_put_schema.load(request.get_json())
            print (data)
        except ValidationError as err:
            return err.messages, 422
        
        if "title" not in data or "id" not in data or "body" not in data:
            return {"message":"bad request"},400
       
        post= Post.query.filter_by(id=data["id"]).first()

        if post != None:
            post.title=data["title"]
            post.body=data["body"]
            db.session.commit()
            return {"message":"Post actualizado correctamente"},200
        else:
            return {"message":"Not Found"},404

class BlogUser(Resource):
    """Clase para obtener los post de un usuario"""
    def get(self,id):
  
        data = id_schema.load(request.view_args)
      
       
        all = Post.query.filter_by(author=data['id'])
        user = User.query.filter_by(id=data['id']).first()
        if user == None:
            return {"message":"Not Found"},404
        else:
            return {"username":user.username,"post":[{"title":i.title,"body":i.body,"id":i.id}for i in all]},200


class UniqueBlog(Resource):
#     data = json.loads(request.data)"""
    """Actualizar un post individual """
    def get(self,id):
 
        data = id_schema.load(request.view_args)
        
  
        post = Post.query.filter_by(id=data['id']).first()
        if post!=None:
            return {"title":post.title,"body":post.body,"id":post.id},200
        else:
            return {"message":"Not Found"},404