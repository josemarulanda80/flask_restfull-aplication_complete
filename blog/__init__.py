
from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from blog.mod.resources import api_bp

#Cargo las configuraicones 


app=Flask(__name__)

app.config.from_object('config.DevelopmentConfig')
app.config.get('UPLOAD_FOLDER')

db =SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(api_bp)
db.create_all()