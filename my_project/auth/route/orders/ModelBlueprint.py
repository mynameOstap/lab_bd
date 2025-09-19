from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import model_controller
from my_project.auth.domain.orders.Model import Model

model_bp = Blueprint('model', __name__, url_prefix='/model')

@model_bp.get('')
def get_all_models() -> Response:
    """
    Get all models
    ---
    tags:
      - Models
    responses:
      200:
        description: List of models
        examples:
          application/json: [
            {"id": 1, "brand_id": 2, "name": "X5"},
            {"id": 2, "brand_id": 3, "name": "A6"}
          ]
    """
    models = model_controller.find_all()
    models_dto = [model.put_into_dto() for model in models]
    return make_response(jsonify(models_dto), HTTPStatus.OK)

@model_bp.post('')
def create_model() -> Response:
    """
    Create a new model
    ---
    tags:
      - Models
    requestBody:
      required: true
      content:
        application/json:
          example:
            brand_id: 2
            name: "X5"
    responses:
      201:
        description: Model created successfully
    """
    content = request.get_json()
    model = Model.create_from_dto(content)
    model_controller.create(model)
    return make_response(jsonify(model.put_into_dto()), HTTPStatus.CREATED)

@model_bp.get('/<int:model_id>')
def get_model(model_id: int) -> Response:
    """
    Get model by ID
    ---
    tags:
      - Models
    parameters:
      - name: model_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Model found
      404:
        description: Model not found
    """
    model = model_controller.find_by_id(model_id)
    if model:
        return make_response(jsonify(model.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Model not found"}), HTTPStatus.NOT_FOUND)

@model_bp.put('/<int:model_id>')
def update_model(model_id: int) -> Response:
    """
    Update model by ID
    ---
    tags:
      - Models
    parameters:
      - name: model_id
        in: path
        required: true
        schema:
          type: integer
    requestBody:
      required: true
      content:
        application/json:
          example:
            brand_id: 3
            name: "A6"
    responses:
      200:
        description: Model updated
    """
    content = request.get_json()
    model = Model.create_from_dto(content)
    model_controller.update(model_id, model)
    return make_response("Model updated", HTTPStatus.OK)

@model_bp.delete('/<int:model_id>')
def delete_model(model_id: int) -> Response:
    """
    Delete model by ID
    ---
    tags:
      - Models
    parameters:
      - name: model_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      204:
        description: Model deleted
    """
    model_controller.delete(model_id)
    return make_response("Model deleted", HTTPStatus.NO_CONTENT)
