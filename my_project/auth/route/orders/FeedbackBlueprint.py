from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import  feedback_controller
from my_project.auth.domain.orders.Feedback import Feedback

feedback_bp = Blueprint('feedback', __name__, url_prefix='/feedback')

@feedback_bp.get('')
def get_all_feedbacks() -> Response:
    feedbacks = feedback_controller.find_all()
    feedbacks_dto = [feedback.put_into_dto() for feedback in feedbacks]
    return make_response(jsonify(feedbacks_dto), HTTPStatus.OK)

@feedback_bp.post('')
def create_feedback() -> Response:
    content = request.get_json()
    feedback = Feedback.create_from_dto(content)
    feedback_controller.create(feedback)
    return make_response(jsonify(feedback.put_into_dto()), HTTPStatus.CREATED)

@feedback_bp.get('/<int:feedback_id>')
def get_feedback(feedback_id: int) -> Response:
    feedback = feedback_controller.find_by_id(feedback_id)
    if feedback:
        return make_response(jsonify(feedback.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Feedback not found"}), HTTPStatus.NOT_FOUND)

@feedback_bp.put('/<int:feedback_id>')
def update_feedback(feedback_id: int) -> Response:
    content = request.get_json()
    feedback = Feedback.create_from_dto(content)
    feedback_controller.update(feedback_id, feedback)
    return make_response("Feedback updated", HTTPStatus.OK)

@feedback_bp.delete('/<int:feedback_id>')
def delete_feedback(feedback_id: int) -> Response:
    feedback_controller.delete(feedback_id)
    return make_response("Feedback deleted", HTTPStatus.NO_CONTENT)
