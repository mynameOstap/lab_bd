# SellerController.py
from typing import List
from my_project.auth.dao.orders.SellerDAO import SellerDAO
from my_project.auth.domain.orders.Seller import Seller

class SellerController:
    _dao = SellerDAO()

    def find_all(self) -> List[Seller]:
        return self._dao.find_all()

    def create(self, seller: Seller) -> None:
        self._dao.create(seller)

    def find_by_id(self, seller_id: int) -> Seller:
        return self._dao.find_by_id(seller_id)

    def update(self, seller_id: int, seller: Seller) -> None:
        self._dao.update(seller_id, seller)

    def delete(self, seller_id: int) -> None:
        self._dao.delete(seller_id)