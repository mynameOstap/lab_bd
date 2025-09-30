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
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  body_type:
                    type: string
                  engine_id:
                    type: integer
                  brand_id:
                    type: integer
            example:
              - id: 1
                body_type: "sedan"
                engine_id: 1
                brand_id: 2
              - id: 2
                body_type: "suv"
                engine_id: 2
                brand_id: 3
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
                description: Type of car body
              engine_id:
                type: integer
                description: ID of the engine
              brand_id:
                type: integer
                description: ID of the brand
          example:
            body_type: "sedan"
            engine_id: 1
            brand_id: 2
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
                body_type:
                  type: string
                engine_id:
                  type: integer
                brand_id:
                  type: integer
            example:
              id: 1
              body_type: "sedan"
              engine_id: 1
              brand_id: 2
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
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                body_type:
                  type: string
                engine_id:
                  type: integer
                brand_id:
                  type: integer
            example:
              id: 1
              body_type: "sedan"
              engine_id: 1
              brand_id: 2
      404:
        description: Model not found
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
            example:
              error: "Model not found"
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
              engine_id:
                type: integer
              brand_id:
                type: integer
          example:
            body_type: "suv"
            engine_id: 2
            brand_id: 3
    responses:
      200:
        description: Model updated
        content:
          application/json:
            schema:
              type: string
            example: "Model updated"
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
        content:
          application/json:
            schema:
              type: string
            example: "Model deleted"
    """
    model_controller.delete(model_id)
    return make_response("Model deleted", HTTPStatus.NO_CONTENT)
