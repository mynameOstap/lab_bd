from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import user_controller

from my_project.auth.domain.orders.User import User

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.get('')
def get_all_users() -> Response:
    users = user_controller.find_all()
    users_dto = [user.put_into_dto() for user in users]
    return make_response(jsonify(users_dto), HTTPStatus.OK)

@user_bp.post('')
def create_user() -> Response:
    content = request.get_json()
    user = User.create_from_dto(content)
    user_controller.create(user)
    return make_response(jsonify(user.put_into_dto()), HTTPStatus.CREATED)

@user_bp.get('/<int:user_id>')
def get_user(user_id: int) -> Response:
    user = user_controller.find_by_id(user_id)
    if user:
        return make_response(jsonify(user.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "User not found"}), HTTPStatus.NOT_FOUND)

@user_bp.put('/<int:user_id>')
def update_user(user_id: int) -> Response:
    content = request.get_json()
    user = User.create_from_dto(content)
    user_controller.update(user_id, user)
    return make_response("User updated", HTTPStatus.OK)

@user_bp.delete('/<int:user_id>')
def delete_user(user_id: int) -> Response:
    user_controller.delete(user_id)
    return make_response("User deleted", HTTPStatus.NO_CONTENT)