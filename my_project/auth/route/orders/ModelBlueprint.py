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
    openapi: 3.0.2
    tags:
      - Models
    responses:
      200:
        description: List of models
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  body_type:
                    type: string
                    enum: ["sedan", "hatchback", "suv", "coupe"]
                    example: "sedan"
                  engine_id:
                    type: integer
                    example: 2
                  brand_id:
                    type: integer
                    example: 3
    """
    models = model_controller.find_all()
    models_dto = [model.put_into_dto() for model in models]
    return make_response(jsonify(models_dto), HTTPStatus.OK)


@model_bp.post('')
def create_model() -> Response:
    """
    Create a new model
    ---
    openapi: 3.0.2
    tags:
      - Models
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - body_type
              - engine_id
              - brand_id
            properties:
              body_type:
                type: string
                enum: ["sedan", "hatchback", "suv", "coupe"]
                example: "suv"
              engine_id:
                type: integer
                example: 1
              brand_id:
                type: integer
                example: 2
    responses:
      201:
        description: Model created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                  example: 10
                body_type:
                  type: string
                  enum: ["sedan", "hatchback", "suv", "coupe"]
                  example: "suv"
                engine_id:
                  type: integer
                  example: 1
                brand_id:
                  type: integer
                  example: 2
    """
    content = request.get_json()
    if not content:
        return make_response(jsonify({"error": "No input data provided"}), HTTPStatus.BAD_REQUEST)

    model = Model.create_from_dto(content)
    model_controller.create(model)
    return make_response(jsonify(model.put_into_dto()), HTTPStatus.CREATED)


@model_bp.get('/<int:model_id>')
def get_model(model_id: int) -> Response:
    """
    Get model by ID
    ---
    openapi: 3.0.2
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
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                  example: 5
                body_type:
                  type: string
                  enum: ["sedan", "hatchback", "suv", "coupe"]
                  example: "sedan"
                engine_id:
                  type: integer
                  example: 2
                brand_id:
                  type: integer
                  example: 3
      404:
        description: Model not found
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: "Model not found"
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
    openapi: 3.0.2
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
          schema:
            type: object
            required:
              - body_type
              - engine_id
              - brand_id
            properties:
              body_type:
                type: string
                enum: ["sedan", "hatchback", "suv", "coupe"]
                example: "hatchback"
              engine_id:
                type: integer
                example: 3
              brand_id:
                type: integer
                example: 1
    responses:
      200:
        description: Model updated
        content:
          application/json:
            schema:
              type: string
              example: "Model updated"
      404:
        description: Model not found
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: "Model not found"
    """
    content = request.get_json()
    if not content:
        return make_response(jsonify({"error": "No input data provided"}), HTTPStatus.BAD_REQUEST)

    model = Model.create_from_dto(content)
    model_controller.update(model_id, model)
    return make_response("Model updated", HTTPStatus.OK)


@model_bp.delete('/<int:model_id>')
def delete_model(model_id: int) -> Response:
    """
    Delete model by ID
    ---
    openapi: 3.0.2
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
      404:
        description: Model not found
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: "Model not found"
    """
    model_controller.delete(model_id)
    return make_response("Model deleted", HTTPStatus.NO_CONTENT)
