from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Location import Location


class LocationDAO(GeneralDAO):
    _domain_type = Location

    def create(self, location: Location) -> None:
        self._session.add(location)
        self._session.commit()

    def find_all(self) -> List[Location]:
        return self._session.query(Location).all()

    def find_by_city(self, city: str) -> List[Location]:
        return self._session.query(Location).filter(Location.city == city).all()