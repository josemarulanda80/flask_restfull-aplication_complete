import json
from blog.database import User,Post,Sale,FileUser,Role
import random
import pytest
from werkzeug.security import generate_password_hash,check_password_hash

randlowercase = f"{chr(random.randint(ord('a'), ord('z')))}{chr(random.randint(ord('a'), ord('z')))}{chr(random.randint(ord('a'), ord('z')))}"

@pytest.fixture(scope='module')
def new_user():
    user = User('patkennedy79@gmail.com', generate_password_hash("FlaskIsAwesome",method="sha256"))
    return user

@pytest.fixture(scope='module')
def new_user_two():
    user = User('admin', 'admin')
    return user


@pytest.fixture(scope='module')
def new_post():
    new_post=Post(author=1,title="El leon de rio de janeiro",body="as")
    return new_post 

@pytest.fixture(scope='module')
def new_sales():
    new_sale=Sale(1,1212,2343)
    return new_sale

@pytest.fixture(scope='module')
def new_files():
    new_file=FileUser(name="imagen6.png",username_id=30,url="http://127.0.0.1:5000/file/imagen6.png")
    return new_file

@pytest.fixture(scope="module")
def new_roles():
    new_role=Role(name="super_user")
    return new_role

@pytest.fixture(scope='module')
def create_new_user():
    json={"username":randlowercase,"password":"12"}
    return json 

@pytest.fixture(scope='module')
def user_existing():
    json={"username":"admin","password":"admin"}
    return json 

@pytest.fixture(scope='module')
def user_delete():
    user = User.query.all()
    last_user=user[-1]
   
    return last_user.id 

@pytest.fixture(scope='module')
def user_bad_json():
    json={"usernae":"admin"}
    return json

@pytest.fixture(scope='module')
def response_user_bad_json():
    json= {"usernae": ["Unknown field."]}
    return json

@pytest.fixture(scope='module')
def new_role():
    json={"name":randlowercase+randlowercase+randlowercase+randlowercase+randlowercase+str(100*random.random())}
    return json

@pytest.fixture(scope='module')
def new_role_update():
    json={"name":randlowercase+randlowercase+randlowercase+str(100*random.random())}
    return json

@pytest.fixture(scope='module')
def id_role():
    rol = Role.query.all()
    return rol[-1].id

@pytest.fixture(scope='module')
def id_new_role():
    rol = Role.query.all()
    return rol[1].id

@pytest.fixture(scope='module')
def name_new_role():
    rol = Role.query.all()
    print(rol[1].name)
    return rol[1].name

@pytest.fixture(scope='module')
def post_user_bad():
    json=  { "author": 0, "body": "python coifwsnciosc", "title": "algo"}
    return json

@pytest.fixture(scope='module')
def post_boby_bad_write():
    json=  { "author": 0, "bdy": "python coifwsnciosc", "title": "algo"}
    return json

@pytest.fixture(scope='module')
def post_correct():
    json=  { "author": 2, "body": "python coifwsnciosc", "title": "algo"}
    return json


@pytest.fixture(scope='module')
def delete_post():
    post=Post.query.all()
    
    return post[-1].id


@pytest.fixture(scope='module')
def modificated_post():
    return {"id":1,"title":"bjkhhjjkjkody","body":"fdf"}


@pytest.fixture(scope='module')
def post_no_body():
    return {"id":2, "title":"bodddy",  "":"fdf"}

@pytest.fixture(scope='module')
def post_body_correct():
    return{"id":18,"title":"bcdcdody","body":"tkdnkcnslckdsnitle"}