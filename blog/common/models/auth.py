from flask_marshmallow import Marshmallow
from blog import ma
from blog.database import User

class UserSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = User
        include_relationships = True
        load_instance = True


        