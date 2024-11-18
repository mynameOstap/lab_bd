# CarController.py
from typing import List

from my_project.auth.dao.orders.CarDAO import CarDAO
from my_project.auth.domain.orders.Car import Car

class CarController:
    _dao = CarDAO()

    def find_all(self) -> List[Car]:
        return self._dao.find_all()

    def create(self, car: Car) -> None:
        self._dao.create(car)

    def find_by_id(self, car_id: int) -> Car:
        return self._dao.find_by_id(car_id)

    def update(self, car_id: int, car: Car) -> None:
        self._dao.update(car_id, car)

    def delete(self, car_id: int) -> None:
        self._dao.delete(car_id)