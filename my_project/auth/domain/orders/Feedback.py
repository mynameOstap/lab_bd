from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Feedback(db.Model, IDto):
    __tablename__ = "feedback"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comment = db.Column(db.String(200), nullable=True)
    rating = db.Column(db.Integer, nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    user = db.relationship('User', backref='feedbacks')
    car = db.relationship('Car', backref='feedbacks')

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "user_id": self.user_id, "comment": self.comment,
                "rating": self.rating, "car_id": self.car_id}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]):
        return Feedback(**dto_dict)