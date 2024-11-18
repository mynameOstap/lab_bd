from typing import List

from my_project.auth.dao import UserDAO
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

class UserService(GeneralService):
    _dao = UserDAO

    def create(self, user: User) -> None:
        self._dao.create(user)

    def get_all_users(self) -> List[User]:
        return self._dao.find_all()

    def get_users_by_name(self, name: str) -> List[User]:
        return self._dao.find_by_name(name)