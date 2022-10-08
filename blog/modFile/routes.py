from flask_restful import Resource
from flask import (request)
from blog.database import Post,User
from marshmallow import ValidationError
from blog import db
from blog.common.utils.Schema_global import IdSchema

class l(Resource):
    def get(self):
        return {"message":"fkj"}