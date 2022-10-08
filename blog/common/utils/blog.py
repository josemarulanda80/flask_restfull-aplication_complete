from marshmallow_sqlalchemy import auto_field
from blog import ma
from blog.database import Post

class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        include_relationships = True
        load_instance = True
        instance_fk=True
    author=auto_field()

class PostPutSchema(ma.Schema):
    fields = ('id','title','body',)