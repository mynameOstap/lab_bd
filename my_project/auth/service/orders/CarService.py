from typing import List

from my_project.auth.dao import CarDAO
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


class CarService(GeneralService):
    _dao = CarDAO

    def create(self, car: Car) -> None:
        self._dao.create(car)

    def get_all_cars(self) -> List[Car]:
        return self._dao.find_all()

    def get_cars_by_price_range(self, min_price: float, max_price: float) -> List[Car]:
        return self._dao.find_by_price_range(min_price, max_price)