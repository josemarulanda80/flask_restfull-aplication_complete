from collections import UserList
from email.policy import default
from blog import db
from datetime import datetime

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(50))
    password=db.Column(db.Text)
    sales=db.relationship("Sale",backref="users",cascade="delete,merge")
    posts=db.relationship('Post',backref="users",cascade="delete,merge")
    file=db.relationship('FileUser',backref="users",cascade="delete,merge",uselist=False)
    roles=db.relationship('Role',backref="users",cascade="delete,merge", useList=True)
    def __init__(self,username,password) -> None:
        self.username = username
        self.password= password
    def __repr__(self) -> str:
        return f'User: {self.username}'


class Sale(db.Model):
    __tablename__="sales"
    id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    username_id=db.Column(db.Integer,db.ForeignKey("users.id",ondelete='CASCADE'))
    venta=db.Column(db.Integer)
    ventas_productos=db.Column(db.Integer)
    created=db.Column(db.DateTime,nullable=False, default=datetime.utcnow)

    def __init__(self,username_id,venta,ventas_productos)-> None:
        self.username_id=username_id
        self.venta=venta
        self.ventas_productos=ventas_productos
    def __repr__(self) -> str:
        return f'Sale: {self.venta}'

class Post(db.Model):
    __tablename__='posts'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    author=db.Column(db.Integer,db.ForeignKey('users.id',ondelete='CASCADE'))
    title = db.Column(db.String(100))
    body= db.Column(db.Text)
    created=db.Column(db.DateTime,nullable=False, default=datetime.utcnow)


    def __init__(self,author,title,body) -> None:
        self.author=author
        self.title=title
        self.body=body
    def __repr__(self) -> str:
        return f'Post: {self.author}'

class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    name = db.Column(db.String(50),default="super_user")
    user_id=db.Column(db.Integer,db.ForeignKey('users.id',ondelete='CASCADE'))

    def __init__(self,name):
        self.name=name
    
    def __repr__(self) -> str:
        return f'Role: {self.name}'