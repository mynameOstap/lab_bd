from typing import List

from my_project.auth.dao import FeedbackDAO
from my_project.auth.dao.orders import (
    CarDAO, TimeSlotDAO, FeedbackDAO, CarImageDAO,
    BrandDAO, EngineDAO, UserDAO, ModelDAO,
    LocationDAO, TestDriveDAO, CompanyDAO,
    SellerDAO
)
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import (
    TimeSlot, Feedback, CarImage, Brand, Engine, User,
    Model, Location, TestDrive, Seller, Car
)


class FeedbackService(GeneralService):
    _dao = FeedbackDAO

    def create(self, feedback: Feedback) -> None:
        self._dao.create(feedback)

    def get_all_feedbacks(self) -> List[Feedback]:
        return self._dao.find_all()

    def get_feedbacks_by_user_id(self, user_id: int) -> List[Feedback]:
        return self._dao.find_by_user_id(user_id)