from flask_restful import Resource
from flask import (json,request,abort,session)
from blog.database import Role, User
from blog.common.models.auth import UserSchema
from werkzeug.security import generate_password_hash,check_password_hash
import jwt,json
from marshmallow import ValidationError
from blog import db
import datetime
from blog import app
from marshmallow import Schema,fields

user_schema = UserSchema()
class BarQuerySchema(Schema):
    id = fields.Str(required=True)
   
schema = BarQuerySchema()

class TodoItem(Resource):
    def get(self, id):
        return {'task': 'Say "Hello, World!"'}


class Auth(Resource):

    # def get(self):
    #     db.session.close()
    #     return "",204

    def post(self):
        try:
            user=user_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 422
        user_name= User.query.filter_by(username = user.username).first()
        if user_name != None:
            return {"message":"Usuario ya registrado"},400
        
        hash_password=generate_password_hash(user.password,method="sha256")
        user.password=hash_password
        rol=Role(name="super_user")
        user.roles.append(rol)
        db.session.add_all([user,rol])
        db.session.commit()
        return {"User_id":user.id},201

    def delete(self):
       
        try:
            data = schema.validate(request.args)
            print(data)
        except ValidationError as err:
            return err.messages, 422
        data=request.args.get('id')
        if data == None or data == "":
            return {"message":"bad request"},400
        user_name = User.query.filter_by(id=data).first()
        if user_name!=None:
            db.session.delete(user_name)
            db.session.commit()
            return "",204
        else:
            return {"message":"archivo no existe"},404
        
class Session(Resource):
    def get(self):
        db.session.close()
        return "",204
    def post(self):
        try:
            user=user_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 422
        user_name= User.query.filter_by(username = user.username).first()
        if user_name == None:
            return {"message":"Usuario no existe"},404
        if check_password_hash(user_name.password, user.password):  
            token = jwt.encode({'public_id': user.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config.get('SECRET_KEY'))             
            return {'token' : token,"id":user_name.id},200
    
  

