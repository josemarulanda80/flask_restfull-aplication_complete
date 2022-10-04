
from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from blog.mod.resources import api_bp

#Cargo las configuraicones 


app=Flask(__name__)

app.config.from_object('config.DevelopmentConfig')
app.config.get('UPLOAD_FOLDER')

app.register_blueprint(api_bp)