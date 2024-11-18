from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import time_slot_controller
from my_project.auth.domain.orders.TimeSlot import TimeSlot


timeslot_bp = Blueprint('timeslot', __name__, url_prefix='/timeslot')

@timeslot_bp.get('')
def get_all_timeslots() -> Response:
    timeslots = time_slot_controller.find_all()
    timeslots_dto = [timeslot.put_into_dto() for timeslot in timeslots]
    return make_response(jsonify(timeslots_dto), HTTPStatus.OK)

@timeslot_bp.post('')
def create_timeslot() -> Response:
    content = request.get_json()
    timeslot = TimeSlot.create_from_dto(content)
    time_slot_controller.create(timeslot)
    return make_response(jsonify(timeslot.put_into_dto()), HTTPStatus.CREATED)

@timeslot_bp.get('/<int:timeslot_id>')
def get_timeslot(timeslot_id: int) -> Response:
    timeslot = time_slot_controller.find_by_id(timeslot_id)
    if timeslot:
        return make_response(jsonify(timeslot.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "TimeSlot not found"}), HTTPStatus.NOT_FOUND)

@timeslot_bp.put('/<int:timeslot_id>')
def update_timeslot(timeslot_id: int) -> Response:
    content = request.get_json()
    timeslot = TimeSlot.create_from_dto(content)
    time_slot_controller.update(timeslot_id, timeslot)
    return make_response("TimeSlot updated", HTTPStatus.OK)

@timeslot_bp.delete('/<int:timeslot_id>')
def delete_timeslot(timeslot_id: int) -> Response:
    time_slot_controller.delete(timeslot_id)
    return make_response("TimeSlot deleted", HTTPStatus.NO_CONTENT)
