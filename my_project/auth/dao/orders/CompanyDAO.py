from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Company import Company


class CompanyDAO(GeneralDAO):
    _domain_type = Company

    def create(self, company: Company) -> None:
        self._session.add(company)
        self._session.commit()

    def find_all(self) -> List[Company]:
        return self._session.query(Company).all()

    def find_by_name(self, name: str) -> Optional[Company]:
        return self._session.query(Company).filter(Company.name == name).first()