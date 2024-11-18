from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Engine import (Engine)


class EngineDAO(GeneralDAO):
    _domain_type = Engine

    def create(self, engine: Engine) -> None:
        self._session.add(engine)
        self._session.commit()

    def find_all(self) -> List[Engine]:
        return self._session.query(Engine).all()

    def find_by_name(self, name: str) -> Optional[Engine]:
        return self._session.query(Engine).filter(Engine.name == name).first()
