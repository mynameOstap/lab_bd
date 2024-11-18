from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Car import Car


class CarDAO(GeneralDAO):
    _domain_type = Car

    def create(self, car: Car) -> None:
        self._session.add(car)
        self._session.commit()

    def find_all(self) -> List[Car]:
        return self._session.query(Car).all()

    def find_by_price_range(self, min_price: float, max_price: float) -> List[Car]:
        return self._session.query(Car).filter(Car.price.between(min_price, max_price)).all()