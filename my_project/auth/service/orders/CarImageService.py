from typing import List

from my_project.auth.dao import CarImageDAO
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


class CarImageService(GeneralService):
    _dao = CarImageDAO

    def create(self, car_image: CarImage) -> None:
        self._dao.create(car_image)

    def get_all_car_images(self) -> List[CarImage]:
        return self._dao.find_all()

    def get_car_images_by_car_id(self, car_id: int) -> List[CarImage]:
        return self._dao.find_by_car_id(car_id)