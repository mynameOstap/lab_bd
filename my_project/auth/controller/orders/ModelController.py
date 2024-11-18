# ModelController.py
from typing import List
from my_project.auth.dao.orders.ModelDAO import ModelDAO
from my_project.auth.domain.orders.Model import Model


class ModelController:
    _dao = ModelDAO()

    def find_all(self) -> List[Model]:
        return self._dao.find_all()

    def create(self, model: Model) -> None:
        self._dao.create(model)

    def find_by_id(self, model_id: int) -> Model:
        return self._dao.find_by_id(model_id)

    def update(self, model_id: int, model: Model) -> None:
        self._dao.update(model_id, model)

    def delete(self, model_id: int) -> None:
        self._dao.delete(model_id)