from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager



app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = 'secret'
db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()


def create_app():
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    
    from app.models import user
    
    from app.controllers.user_controller import UserController
    from app.controllers.auth_controller import AuthController
    
    app.register_blueprint(UserController.user_controller, url_prefix="/api/v1")
    app.register_blueprint(AuthController.auth_controller, url_prefix="/api/v1")
    
    with app.app_context():
       db.create_all()
       
    return app