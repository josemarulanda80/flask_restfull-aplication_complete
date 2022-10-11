from flask_restful import Resource
from flask import (request,send_from_directory)
from blog.database import User,FileUser
from marshmallow import ValidationError
from blog import db
from blog.common.utils.Schema_global import IdSchema, NameFileSchema
from blog import app
from os import  getcwd, path,remove

name_file_image=NameFileSchema()
id_schema=IdSchema()

class FileUrl(Resource):
    """Clase para obtener url de las imagenes guardades en la carpeta estatica"""
    def get(self,name_file):
        print(app.config.get('UPLOAD_FOLDER'))
        data = name_file_image.load(request.view_args)
        return send_from_directory(app.config.get('UPLOAD_FOLDER'),path=data['name_file'],as_attachment=False)


class FileUserDownload(Resource):
    """Clase para descargar las imagenes en la base de datos"""
    def get(self,name_file):
        data = name_file_image.load(request.view_args)
    # print(send_from_directory(PATH_FILE,path=name_file,as_attachment=False))
        return send_from_directory(app.config.get('UPLOAD_FOLDER'),path=data['name_file'],as_attachment=True)

    
class FileUserPostPut(Resource):
    """Clase para agrega una imagen o actualizarla"""
    def post(self,id):
        print("Hola2")
        file=request.files['file']
        print(request.files)
        # data= jsonify({"nombre":file.filename,"id":request.args.get('id')})
        data = id_schema.load(request.view_args)
        print("Hola")
        print(file.filename)
        print(data)
        new_file=FileUser(name=file.filename,username_id=data['id'],url="http://127.0.0.1:5000/files/{file.filename}") 
        user = User.query.filter_by(id=data['id']).first()
        if user ==None:
            return {"message":"Bad request"},400
        else:
            image = FileUser.query.filter_by(username_id=data["id"]).first()
            if image != None:
                return self.put(image,file,user)
            else:
                file.save(app.config.get('UPLOAD_FOLDER') + file.filename)
                db.session.add(new_file)
                db.session.commit()
                return {"message":"imagen agregada al usuario con exito"},201  
    def put(self,image,file,user):
            if path.isfile(app.config.get('UPLOAD_FOLDER')+image.name)==True and image.name != "user.png":
                remove(app.config.get('UPLOAD_FOLDER')+image.name)
            file.save(app.config.get('UPLOAD_FOLDER') + file.filename)
            image.name=file.filename
            image.url=f"http://127.0.0.1:5000/files/{file.filename}"
            image.usenrma_id=user.id
            db.session.commit()
            return {"message":"imagen del usuario actualizada con exito"},200

class UserImg(Resource):
        """Clase para actualizar la información de una imagen"""
        def get(self,id):
            data = id_schema.load(request.view_args)
            file =FileUser.query.filter_by(username_id=data['id']).first()
            if file == None:
                return {"message":"Not Found"}
            else:
                return {"url":file.url},200
