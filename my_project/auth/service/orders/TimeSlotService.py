from typing import List

from my_project.auth.dao import TimeSlotDAO
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

class TimeSlotService(GeneralService):
    _dao = TimeSlotDAO

    def create(self, time_slot: TimeSlot) -> None:
        self._dao.create(time_slot)

    def get_all_time_slots(self) -> List[TimeSlot]:
        return self._dao.find_all()