
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

app = Flask(__name__)

#Cargo todas las configuraciones

app.config.from_object('config.DevelopmentConfig')
app.config.get('UPLOAD_FOLDER')
ma = Marshmallow()
ma.init_app(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#Importar vistas
from blog.modUser.resources import api_bp
from blog.modPost.resources import api_post
app.register_blueprint(api_bp)
app.register_blueprint(api_post)
db.create_all()
