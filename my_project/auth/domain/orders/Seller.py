from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Seller(db.Model, IDto):
    __tablename__ = "seller"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    kind = db.Column(db.Enum("dealer", "person"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=True)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    user = db.relationship('User', backref='sellers')
    company = db.relationship('Company', backref='sellers')
    location = db.relationship('Location', backref='sellers')


    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "kind": self.kind, "user_id": self.user_id,
                "company_id": self.company_id, "location_id": self.location_id}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]):
        return Seller(**dto_dict)