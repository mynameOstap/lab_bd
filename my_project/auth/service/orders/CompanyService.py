from typing import List

from my_project.auth.dao import CompanyDAO
from my_project.auth.dao.orders import (
    CarDAO, TimeSlotDAO, FeedbackDAO, CarImageDAO,
    BrandDAO, EngineDAO, UserDAO, ModelDAO,
    LocationDAO, TestDriveDAO, CompanyDAO,
    SellerDAO
)
from my_project.auth.domain.orders.Company import Company
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import (
    TimeSlot, Feedback, CarImage,  Brand, Engine, User,
    Model, Location, TestDrive, Seller, Car
)

class CompanyService(GeneralService):
    _dao = CompanyDAO

    def create(self, company: Company) -> None:
        self._dao.create(company)

    def get_all_companies(self) -> List[Company]:
        return self._dao.find_all()

    def get_company_by_name(self, name: str) -> List[Company]:
        return self._dao.find_by_name(name)