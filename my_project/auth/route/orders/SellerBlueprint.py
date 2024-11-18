from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import seller_controller
from my_project.auth.domain.orders.Seller import Seller

seller_bp = Blueprint('seller', __name__, url_prefix='/seller')

@seller_bp.get('')
def get_all_sellers() -> Response:
    sellers = seller_controller.find_all()
    sellers_dto = [seller.put_into_dto() for seller in sellers]
    return make_response(jsonify(sellers_dto), HTTPStatus.OK)

@seller_bp.post('')
def create_seller() -> Response:
    content = request.get_json()
    seller = Seller.create_from_dto(content)
    seller_controller.create(seller)
    return make_response(jsonify(seller.put_into_dto()), HTTPStatus.CREATED)

@seller_bp.get('/<int:seller_id>')
def get_seller(seller_id: int) -> Response:
    seller = seller_controller.find_by_id(seller_id)
    if seller:
        return make_response(jsonify(seller.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Seller not found"}), HTTPStatus.NOT_FOUND)

@seller_bp.put('/<int:seller_id>')
def update_seller(seller_id: int) -> Response:
    content = request.get_json()
    seller = Seller.create_from_dto(content)
    seller_controller.update(seller_id, seller)
    return make_response("Seller updated", HTTPStatus.OK)

@seller_bp.delete('/<int:seller_id>')
def delete_seller(seller_id: int) -> Response:
    seller_controller.delete(seller_id)
    return make_response("Seller deleted", HTTPStatus.NO_CONTENT)