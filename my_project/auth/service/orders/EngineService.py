from typing import List

from my_project.auth.dao import EngineDAO
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

class EngineService(GeneralService):
    _dao = EngineDAO

    def create(self, engine: Engine) -> None:
        self._dao.create(engine)

    def get_all_engines(self) -> List[Engine]:
        return self._dao.find_all()

    def get_engine_by_name(self, name: str) -> List[Engine]:
        return self._dao.find_by_name(name)