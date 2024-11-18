# TestDriveController.py
from typing import List
from my_project.auth.dao.orders.TestDriveDAO import TestDriveDAO
from my_project.auth.domain.orders.TestDrive import TestDrive


class TestDriveController:
    _dao = TestDriveDAO()

    def find_all(self) -> List[TestDrive]:
        return self._dao.find_all()

    def create(self, test_drive: TestDrive) -> None:
        self._dao.create(test_drive)

    def find_by_id(self, test_drive_id: int) -> TestDrive:
        return self._dao.find_by_id(test_drive_id)

    def update(self, test_drive_id: int, test_drive: TestDrive) -> None:
        self._dao.update(test_drive_id, test_drive)

    def delete(self, test_drive_id: int) -> None:
        self._dao.delete(test_drive_id)