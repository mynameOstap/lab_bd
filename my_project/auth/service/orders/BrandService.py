from typing import List

from my_project.auth.dao import BrandDAO
from my_project.auth.dao.orders import (
    CarDAO, TimeSlotDAO, FeedbackDAO, CarImageDAO,
    BrandDAO, EngineDAO, UserDAO, ModelDAO,
    LocationDAO, TestDriveDAO, CompanyDAO,
    SellerDAO
)
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import (
    TimeSlot, Feedback, CarImage,  Brand, Engine, User,
    Model, Location, TestDrive, Seller, Car
)

class BrandService(GeneralService):
    _dao = BrandDAO

    def create(self, brand: Brand) -> None:
        self._dao.create(brand)

    def get_all_brands(self) -> List[Brand]:
        return self._dao.find_all()

    def get_brand_by_name(self, name: str) -> List[Brand]:
        return self._dao.find_by_name(name)