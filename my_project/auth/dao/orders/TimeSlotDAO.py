from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.TimeSlot import TimeSlot


class TimeSlotDAO(GeneralDAO):
    _domain_type = TimeSlot

    def create(self, time_slot: TimeSlot) -> None:
        self._session.add(time_slot)
        self._session.commit()

    def find_all(self) -> List[TimeSlot]:
        return self._session.query(TimeSlot).all()