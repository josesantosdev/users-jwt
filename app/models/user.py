from sqlalchemy import Column, BigInteger, String
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow import fields

from app import db, ma


class User(db.Model):
    __tablename__ = 'User'
    id_user = Column(BigInteger, primary_key=True)
    user_name = Column(String(128), nullable=False)
    login = Column(String(128), nullable=False)
    password = Column(String(256), nullable=False)
    user_role = Column(BigInteger, default=1)

    def __init__(self,  user_name, login, password, user_role):
        self.user_name = user_name
        self.login = login
        self.password = generate_password_hash(password)
        self.user_role = user_role


    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'<User: {self.login}'


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True

        id_user = fields.Integer()
        user_name = fields.Str(required=True)
        login = fields.Str(required=True)
        password = fields.Str(load_only=True, required=True)
        user_role = fields.Integer()
