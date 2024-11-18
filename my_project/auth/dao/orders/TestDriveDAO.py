from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.TestDrive import TestDrive


class TestDriveDAO(GeneralDAO):
    _domain_type = TestDrive

    def create(self, test_drive: TestDrive) -> None:
        self._session.add(test_drive)
        self._session.commit()

    def find_all(self) -> List[TestDrive]:
        return self._session.query(TestDrive).all()