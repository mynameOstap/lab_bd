from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto



class TestDrive(db.Model, IDto):
    __tablename__ = "test_drive"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    location = db.relationship('Location', backref='test_drives')

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "location_id": self.location_id}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]):
        return TestDrive(**dto_dict)