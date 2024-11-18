# FeedbackController.py
from typing import List
from my_project.auth.dao.orders.FeedbackDAO import FeedbackDAO
from my_project.auth.domain.orders.Feedback import Feedback


class FeedbackController:
    _dao = FeedbackDAO()

    def find_all(self) -> List[Feedback]:
        return self._dao.find_all()

    def create(self, feedback: Feedback) -> None:
        self._dao.create(feedback)

    def find_by_id(self, feedback_id: int) -> Feedback:
        return self._dao.find_by_id(feedback_id)

    def update(self, feedback_id: int, feedback: Feedback) -> None:
        self._dao.update(feedback_id, feedback)

    def delete(self, feedback_id: int) -> None:
        self._dao.delete(feedback_id)
