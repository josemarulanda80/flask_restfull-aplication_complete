
from flask_restful import Resource
from flask import (json,request,abort,session)
import sqlalchemy
from blog.database import Role, User
from blog.common.models.auth import RoleSchema, UserSchema
from werkzeug.security import generate_password_hash,check_password_hash
import jwt,json
from marshmallow import ValidationError
from blog import db
import datetime
from blog import app


user_schema = UserSchema()
role_schema= RoleSchema()

class Auth(Resource):
    """Clase para guardar un usuario que se registre a la plataforma y tambien para borrarlo"""

    def post(self):
        try:
            user=user_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 422
        except TypeError:
            return {"message":"bad request"},400
        user_name= User.query.filter_by(username = user.username).first()
        if user_name != None:
            return {"message":"Usuario ya registrado"},400

        hash_password=generate_password_hash(user.password,method="sha256")
        user.password=hash_password
        rol= Role.query.filter_by(name="super_user").first()
        if (rol == None):
            rol=Role(name="super_user")
        user.roles.append(rol)
        db.session.add_all([user,rol])
        db.session.commit()
        return {"User_id":user.id},201

    def delete(self):
        data=request.args.get('id')
        if data == None or data == "":
            return {"message":"bad request"}, 400
        user_name = User.query.filter_by(id=data).first()
        if user_name!=None:
            db.session.delete(user_name)
            db.session.commit()
            return "",204
        else:
            return {"message":"archivo no existe"},404

class Session(Resource):
    """Clase relacionada con enviar cerrar sesion y loguear usuarios"""
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

class AddRoles(Resource):
    """Clase para obtener roles, crear roles y borrarlos"""
    def get(self):
        roles = Role.query.all()
        return {"roles":[{"id": i.id, "name":i.name} for i in roles ]},200

    def post(self):
        try:
            role=role_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 422

        role_name= Role.query.filter_by(name = role.name).first()
        if role_name != None:
            return {"message":"Role ya registrado"},400

        db.session.add(role)
        db.session.commit()
        return {"Role_id":role.id},201

    def delete(self):
        data=request.args.get('id')
        if data == None or data == "":
            return {"message":"bad request"},400
        role_name = Role.query.filter_by(id=data).first()
        if role_name!=None:
            db.session.delete(role_name)
            db.session.commit()
            return "",204
        else:
            return {"message":"archivo no existe"},404


class UpdateRoles(Resource):

    def put(self,id_rol):
        try:
            role=role_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 422

        role_name= Role.query.filter_by(id = id_rol).first()
        if role_name == None:
            return {"message":"Not found"},404

        try:
            role_name.name=role.name
            db.session.commit()
            return {"message":"rol actualizado"},200
        except sqlalchemy.exc.IntegrityError:
            return {"message":"No puede cambiar el rol a uno ya existente"},400

    def post(self,id_rol):
        data=json.loads(request.data)
        if "id_user" not in data or data["id_user"]=="":
            return {"message":"Bat request"},400
        user = User.query.filter_by(id=data["id_user"]).first()
        role = Role.query.filter_by(id=id_rol).first()
        if user == None or role ==None:
            return {"message":"Not Founf"},404
        user.roles.append(role)
        db.session.add_all([user,role])
        db.session.commit()
        return {"user":user.id},201
    