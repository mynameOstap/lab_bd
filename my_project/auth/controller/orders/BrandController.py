# BrandController.py
from typing import List
from my_project.auth.dao.orders.BrandDAO import BrandDAO
from my_project.auth.domain.orders.Brand import Brand


class BrandController:
    _dao = BrandDAO()

    def find_all(self) -> List[Brand]:
        return self._dao.find_all()

    def create(self, brand: Brand) -> None:
        self._dao.create(brand)

    def find_by_id(self, brand_id: int) -> Brand:
        return self._dao.find_by_id(brand_id)

    def update(self, brand_id: int, brand: Brand) -> None:
        self._dao.update(brand_id, brand)

    def delete(self, brand_id: int) -> None:
        self._dao.delete(brand_id)