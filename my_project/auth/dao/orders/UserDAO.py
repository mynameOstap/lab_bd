from typing import List, Optional

from sqlalchemy.orm import joinedload

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.User import User


class UserDAO(GeneralDAO):
    _domain_type = User

    def create(self, user: User) -> None:
        self._session.add(user)
        self._session.commit()

    def find_all(self) -> List[User]:
        return self._session.query(User).all()

    def find_by_name(self, name: str) -> List[User]:
        return self._session.query(User).filter(User.name == name).all()
