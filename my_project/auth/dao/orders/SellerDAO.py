from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Seller import Seller


class SellerDAO(GeneralDAO):
    _domain_type = Seller

    def create(self, seller: Seller) -> None:
        self._session.add(seller)
        self._session.commit()

    def find_all(self) -> List[Seller]:
        return self._session.query(Seller).all()