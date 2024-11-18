from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import company_controller
from my_project.auth.domain.orders.Company import Company


company_bp = Blueprint('company', __name__, url_prefix='/company')

@company_bp.get('')
def get_all_companies() -> Response:
    companies = company_controller.find_all()
    companies_dto = [company.put_into_dto() for company in companies]
    return make_response(jsonify(companies_dto), HTTPStatus.OK)

@company_bp.post('')
def create_company() -> Response:
    content = request.get_json()
    company = Company.create_from_dto(content)
    company_controller.create(company)
    return make_response(jsonify(company.put_into_dto()), HTTPStatus.CREATED)

@company_bp.get('/<int:company_id>')
def get_company(company_id: int) -> Response:
    company = company_controller.find_by_id(company_id)
    if company:
        return make_response(jsonify(company.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Company not found"}), HTTPStatus.NOT_FOUND)

@company_bp.put('/<int:company_id>')
def update_company(company_id: int) -> Response:
    content = request.get_json()
    company = Company.create_from_dto(content)
    company_controller.update(company_id, company)
    return make_response("Company updated", HTTPStatus.OK)

@company_bp.delete('/<int:company_id>')
def delete_company(company_id: int) -> Response:
    company_controller.delete(company_id)
    return make_response("Company deleted", HTTPStatus.NO_CONTENT)
