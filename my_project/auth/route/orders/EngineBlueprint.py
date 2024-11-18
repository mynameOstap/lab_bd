from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import  engine_controller
from my_project.auth.domain.orders.Engine import Engine

engine_bp = Blueprint('engine', __name__, url_prefix='/engine')

@engine_bp.get('')
def get_all_engines() -> Response:
    engines = engine_controller.find_all()
    engines_dto = [engine.put_into_dto() for engine in engines]
    return make_response(jsonify(engines_dto), HTTPStatus.OK)

@engine_bp.post('')
def create_engine() -> Response:
    content = request.get_json()
    engine = Engine.create_from_dto(content)
    engine_controller.create(engine)
    return make_response(jsonify(engine.put_into_dto()), HTTPStatus.CREATED)

@engine_bp.get('/<int:engine_id>')
def get_engine(engine_id: int) -> Response:
    engine = engine_controller.find_by_id(engine_id)
    if engine:
        return make_response(jsonify(engine.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Engine not found"}), HTTPStatus.NOT_FOUND)

@engine_bp.put('/<int:engine_id>')
def update_engine(engine_id: int) -> Response:
    content = request.get_json()
    engine = Engine.create_from_dto(content)
    engine_controller.update(engine_id, engine)
    return make_response("Engine updated", HTTPStatus.OK)

@engine_bp.delete('/<int:engine_id>')
def delete_engine(engine_id: int) -> Response:
    engine_controller.delete(engine_id)
    return make_response("Engine deleted", HTTPStatus.NO_CONTENT)
