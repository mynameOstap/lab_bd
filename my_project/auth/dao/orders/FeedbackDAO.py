from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Feedback import Feedback


class FeedbackDAO(GeneralDAO):
    _domain_type = Feedback

    def create(self, feedback: Feedback) -> None:
        self._session.add(feedback)
        self._session.commit()

    def find_all(self) -> List[Feedback]:
        return self._session.query(Feedback).all()

    def find_by_user_id(self, user_id: int) -> List[Feedback]:
        return self._session.query(Feedback).filter(Feedback.user_id == user_id).all()
