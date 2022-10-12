
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
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
from blog.modFile.resources import api_file
app.register_blueprint(api_bp)
app.register_blueprint(api_post)
app.register_blueprint(api_file)
db.create_all()
