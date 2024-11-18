from typing import List, Optional

from sqlalchemy.orm import joinedload

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Model import Model


class ModelDAO(GeneralDAO):
    _domain_type = Model

    def create(self, model: Model) -> None:
        self._session.add(model)
        self._session.commit()

    def find_all(self) -> List[Model]:
        return self._session.query(Model).all()

    def find_by_body_type(self, body_type: str) -> List[Model]:
        return self._session.query(Model).filter(Model.body_type == body_type).all()