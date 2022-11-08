import os

#Configuration base
class Config:
    #database configuration
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:jos84mar19@localhost:3306/blog"

class ProductionConfig(Config):
    DEBUG=False

class DevelopmentConfig(Config):
    #location folder  statics files
    UPLOAD_FOLDER=os.path.realpath('.')+ '/blog/templates/static/images/'
    #secret key is util by Auth and security
    SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
    DEBUG=True
    TESTING=True
    