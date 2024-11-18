from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import car_controller
from my_project.auth.domain.orders.Car import Car


car_bp = Blueprint('car', __name__, url_prefix='/car')

@car_bp.get('')
def get_all_cars() -> Response:
    cars = car_controller.find_all()
    cars_dto = [car.put_into_dto() for car in cars]
    return make_response(jsonify(cars_dto), HTTPStatus.OK)

@car_bp.post('')
def create_car() -> Response:
    content = request.get_json()
    car = Car.create_from_dto(content)
    car_controller.create(car)
    return make_response(jsonify(car.put_into_dto()), HTTPStatus.CREATED)

@car_bp.get('/<int:car_id>')
def get_car(car_id: int) -> Response:
    car = car_controller.find_by_id(car_id)
    if car:
        return make_response(jsonify(car.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Car not found"}), HTTPStatus.NOT_FOUND)

@car_bp.put('/<int:car_id>')
def update_car(car_id: int) -> Response:
    content = request.get_json()
    car = Car.create_from_dto(content)
    car_controller.update(car_id, car)
    return make_response("Car updated", HTTPStatus.OK)

@car_bp.delete('/<int:car_id>')
def delete_car(car_id: int) -> Response:
    car_controller.delete(car_id)
    return make_response("Car deleted", HTTPStatus.NO_CONTENT)