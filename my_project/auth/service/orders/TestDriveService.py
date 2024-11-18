from typing import List

from my_project.auth.dao import TestDriveDAO
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


class TestDriveService(GeneralService):
    _dao = TestDriveDAO

    def create(self, test_drive: TestDrive) -> None:
        self._dao.create(test_drive)

    def get_all_test_drives(self) -> List[TestDrive]:
        return self._dao.find_all()