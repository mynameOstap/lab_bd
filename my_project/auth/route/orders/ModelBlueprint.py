from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import model_controller

from my_project.auth.domain.orders.Model import Model

model_bp = Blueprint('model', __name__, url_prefix='/model')

@model_bp.get('')
def get_all_models() -> Response:
    models = model_controller.find_all()
    models_dto = [model.put_into_dto() for model in models]
    return make_response(jsonify(models_dto), HTTPStatus.OK)

@model_bp.post('')
def create_model() -> Response:
    content = request.get_json()
    model = Model.create_from_dto(content)
    model_controller.create(model)
    return make_response(jsonify(model.put_into_dto()), HTTPStatus.CREATED)

@model_bp.get('/<int:model_id>')
def get_model(model_id: int) -> Response:
    model = model_controller.find_by_id(model_id)
    if model:
        return make_response(jsonify(model.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Model not found"}), HTTPStatus.NOT_FOUND)

@model_bp.put('/<int:model_id>')
def update_model(model_id: int) -> Response:
    content = request.get_json()
    model = Model.create_from_dto(content)
    model_controller.update(model_id, model)
    return make_response("Model updated", HTTPStatus.OK)

@model_bp.delete('/<int:model_id>')
def delete_model(model_id: int) -> Response:
    model_controller.delete(model_id)
    return make_response("Model deleted", HTTPStatus.NO_CONTENT)