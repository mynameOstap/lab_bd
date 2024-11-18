from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import location_controller
from my_project.auth.domain.orders.Location import Location

location_bp = Blueprint('location', __name__, url_prefix='/location')

@location_bp.get('')
def get_all_locations() -> Response:
    locations = location_controller.find_all()
    locations_dto = [location.put_into_dto() for location in locations]
    return make_response(jsonify(locations_dto), HTTPStatus.OK)

@location_bp.post('')
def create_location() -> Response:
    content = request.get_json()
    location = Location.create_from_dto(content)
    location_controller.create(location)
    return make_response(jsonify(location.put_into_dto()), HTTPStatus.CREATED)

@location_bp.get('/<int:location_id>')
def get_location(location_id: int) -> Response:
    location = location_controller.find_by_id(location_id)
    if location:
        return make_response(jsonify(location.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Location not found"}), HTTPStatus.NOT_FOUND)

@location_bp.put('/<int:location_id>')
def update_location(location_id: int) -> Response:
    content = request.get_json()
    location = Location.create_from_dto(content)
    location_controller.update(location_id, location)
    return make_response("Location updated", HTTPStatus.OK)

@location_bp.delete('/<int:location_id>')
def delete_location(location_id: int) -> Response:
    location_controller.delete(location_id)
    return make_response("Location deleted", HTTPStatus.NO_CONTENT)