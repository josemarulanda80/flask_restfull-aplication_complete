from marshmallow_sqlalchemy import auto_field
from blog import ma
from blog.database import Post
from marshmallow import Schema, fields

class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        include_relationships = True
        load_instance = True
        instance_fk=True
    author=auto_field()

class PostPutSchema(ma.Schema):
    id = fields.Int()
    body = fields.Str()
    title = fields.Str()