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
        include_fk =True
        include_relationships=True
        load_instance=True
    


        