# EngineController.py
from typing import List
from my_project.auth.dao.orders.EngineDAO import EngineDAO
from my_project.auth.domain.orders.Engine import Engine


class EngineController:
    _dao = EngineDAO()

    def find_all(self) -> List[Engine]:
        return self._dao.find_all()

    def create(self, engine: Engine) -> None:
        self._dao.create(engine)

    def find_by_id(self, engine_id: int) -> Engine:
        return self._dao.find_by_id(engine_id)

    def update(self, engine_id: int, engine: Engine) -> None:
        self._dao.update(engine_id, engine)

    def delete(self, engine_id: int) -> None:
        self._dao.delete(engine_id)