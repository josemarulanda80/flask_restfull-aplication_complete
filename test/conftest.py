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