from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import car_image_controller
from my_project.auth.domain.orders.CarImage import CarImage

carimage_bp = Blueprint('carimage', __name__, url_prefix='/carimage')

@carimage_bp.get('')
def get_all_carimages() -> Response:
    carimages = car_image_controller.find_all()
    carimages_dto = [carimage.put_into_dto() for carimage in carimages]
    return make_response(jsonify(carimages_dto), HTTPStatus.OK)

@carimage_bp.post('')
def create_carimage() -> Response:
    content = request.get_json()
    carimage = CarImage.create_from_dto(content)
    car_image_controller.create(carimage)
    return make_response(jsonify(carimage.put_into_dto()), HTTPStatus.CREATED)

@carimage_bp.get('/<int:carimage_id>')
def get_carimage(carimage_id: int) -> Response:
    carimage = car_image_controller.find_by_id(carimage_id)
    if carimage:
        return make_response(jsonify(carimage.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "CarImage not found"}), HTTPStatus.NOT_FOUND)

@carimage_bp.put('/<int:carimage_id>')
def update_carimage(carimage_id: int) -> Response:
    content = request.get_json()
    carimage = CarImage.create_from_dto(content)
    car_image_controller.update(carimage_id, carimage)
    return make_response("CarImage updated", HTTPStatus.OK)

@carimage_bp.delete('/<int:carimage_id>')
def delete_carimage(carimage_id: int) -> Response:
    car_image_controller.delete(carimage_id)
    return make_response("CarImage deleted", HTTPStatus.NO_CONTENT)