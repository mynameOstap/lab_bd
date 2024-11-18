# TimeSlotController.py
from typing import List

from my_project.auth.dao.orders.TimeSlotDAO import TimeSlotDAO
from my_project.auth.domain.orders.TimeSlot import TimeSlot


class TimeSlotController:
    _dao = TimeSlotDAO()

    def find_all(self) -> List[TimeSlot]:
        return self._dao.find_all()

    def create(self, time_slot: TimeSlot) -> None:
        self._dao.create(time_slot)

    def find_by_id(self, time_slot_id: int) -> TimeSlot:
        return self._dao.find_by_id(time_slot_id)

    def update(self, time_slot_id: int, time_slot: TimeSlot) -> None:
        self._dao.update(time_slot_id, time_slot)

    def delete(self, time_slot_id: int) -> None:
        self._dao.delete(time_slot_id)
