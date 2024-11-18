# CompanyController.py
from typing import List

from my_project.auth.dao.orders.CompanyDAO import CompanyDAO
from my_project.auth.domain.orders.Company import Company


class CompanyController:
    _dao = CompanyDAO()

    def find_all(self) -> List[Company]:
        return self._dao.find_all()

    def create(self, company: Company) -> None:
        self._dao.create(company)

    def find_by_id(self, company_id: int) -> Company:
        return self._dao.find_by_id(company_id)

    def update(self, company_id: int, company: Company) -> None:
        self._dao.update(company_id, company)

    def delete(self, company_id: int) -> None:
        self._dao.delete(company_id)