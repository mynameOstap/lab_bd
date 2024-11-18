from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class TimeSlot(db.Model, IDto):
    __tablename__ = "timeslot"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.DATETIME, nullable=False)
    test_drive_id = db.Column(db.Integer, db.ForeignKey('test_drive.id'), nullable=False)
    test_drive = db.relationship('TestDrive', backref='timeslots')

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "time": self.time, "test_drive_id": self.test_drive_id}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]):
        return TimeSlot(**dto_dict)