from xml.etree.ElementInclude import include
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import auto_field
from sqlalchemy import true
from blog import ma
from blog.database import Role, User

class UserSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = User
        include_relationships = True
        load_instance = True

class RoleSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model=Role
        include_relationships=True
        load_instance=True
    


        