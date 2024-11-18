from typing import List

from my_project.auth.dao import ModelDAO
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

class ModelService(GeneralService):
    _dao = ModelDAO()

    def create(self, model: Model) -> None:
        self._dao.create(model)

    def get_all_models(self) -> List[Model]:
        return self._dao.find_all()

    def get_models_by_body_type(self, body_type: str) -> List[Model]:
        return self._dao.find_by_body_type(body_type)
