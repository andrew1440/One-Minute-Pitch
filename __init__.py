from flask import Flask
From flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlachemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import flask_mail


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Boostrap()
db = SQLAlchemy()
photos = UploadSet ('photos',IMAGES)
mail = mail()

