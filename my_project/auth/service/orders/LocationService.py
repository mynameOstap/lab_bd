from typing import List

from my_project.auth.dao import LocationDAO
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


class LocationService(GeneralService):
    _dao = LocationDAO

    def create(self, location: Location) -> None:
        self._dao.create(location)

    def get_all_locations(self) -> List[Location]:
        return self._dao.find_all()

    def get_locations_by_city(self, city: str) -> List[Location]:
        return self._dao.find_by_city(city)