from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import test_drive_controller
from my_project.auth.domain.orders.TestDrive import TestDrive

testdrive_bp = Blueprint('testdrive', __name__, url_prefix='/testdrive')

@testdrive_bp.get('')
def get_all_testdrives() -> Response:
    testdrives = test_drive_controller.find_all()
    testdrives_dto = [testdrive.put_into_dto() for testdrive in testdrives]
    return make_response(jsonify(testdrives_dto), HTTPStatus.OK)

@testdrive_bp.post('')
def create_testdrive() -> Response:
    content = request.get_json()
    testdrive = TestDrive.create_from_dto(content)
    test_drive_controller.create(testdrive)
    return make_response(jsonify(testdrive.put_into_dto()), HTTPStatus.CREATED)

@testdrive_bp.get('/<int:testdrive_id>')
def get_testdrive(testdrive_id: int) -> Response:
    testdrive = test_drive_controller.find_by_id(testdrive_id)
    if testdrive:
        return make_response(jsonify(testdrive.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "TestDrive not found"}), HTTPStatus.NOT_FOUND)

@testdrive_bp.put('/<int:testdrive_id>')
def update_testdrive(testdrive_id: int) -> Response:
    content = request.get_json()
    testdrive = TestDrive.create_from_dto(content)
    test_drive_controller.update(testdrive_id, testdrive)
    return make_response("TestDrive updated", HTTPStatus.OK)

@testdrive_bp.delete('/<int:testdrive_id>')
def delete_testdrive(testdrive_id: int) -> Response:
    test_drive_controller.delete(testdrive_id)
    return make_response("TestDrive deleted", HTTPStatus.NO_CONTENT)
