# CarImageController.py
from typing import List

from my_project.auth.dao.orders.CarImageDAO import CarImageDAO
from my_project.auth.domain.orders.CarImage import CarImage

class CarImageController:
    _dao = CarImageDAO()

    def find_all(self) -> List[CarImage]:
        return self._dao.find_all()

    def create(self, car_image: CarImage) -> None:
        self._dao.create(car_image)

    def find_by_id(self, car_image_id: int) -> CarImage:
        return self._dao.find_by_id(car_image_id)

    def update(self, car_image_id: int, car_image: CarImage) -> None:
        self._dao.update(car_image_id, car_image)

    def delete(self, car_image_id: int) -> None:
        self._dao.delete(car_image_id)
