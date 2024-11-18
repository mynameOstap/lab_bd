from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.CarImage import CarImage


class CarImageDAO(GeneralDAO):
    _domain_type = CarImage

    def create(self, car_image: CarImage) -> None:
        self._session.add(car_image)
        self._session.commit()

    def find_all(self) -> List[CarImage]:
        return self._session.query(CarImage).all()

    def find_by_car_id(self, car_id: int) -> List[CarImage]:
        return self._session.query(CarImage).filter(CarImage.car_id == car_id).all()