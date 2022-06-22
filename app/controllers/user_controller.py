from app.models.user import User, UserSchema
from flask import Blueprint, jsonify, request, render_template, make_response
from flask_jwt_extended import jwt_required


class UserController:
    user_controller = Blueprint(name='user_controller', import_name=__name__)

    @user_controller.route('/users', methods=['GET'])
    @jwt_required()
    def get_user_list():
        user_list = User.query.all()
        user_schema = UserSchema(many=True)
        users = user_schema.dump(user_list)
        return make_response(jsonify({
            "Users" : users
        })), 200

    @user_controller.route('/users/<id>', methods=['GET'])
    @jwt_required()
    def get_user(id):
        user =  User.query.filter_by(id_user=id).first_or_404()
        user_schema = UserSchema()
        users = user_schema.dump(user)
        return make_response(jsonify({
            "User": users
        })), 200
    
    @user_controller.route('/', methods=['GET'])
    def index():
        return render_template('index.html')