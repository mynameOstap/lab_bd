from typing import List

from my_project.auth.dao import SellerDAO
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


class SellerService(GeneralService):
    _dao = SellerDAO

    def create(self, seller: Seller) -> None:
        self._dao.create(seller)

    def get_all_sellers(self) -> List[Seller]:
        return self._dao.find_all()