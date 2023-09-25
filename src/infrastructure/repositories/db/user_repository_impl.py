from injector import inject

from src.domain.repositories.db.user_repository import UserRepository
from src.infrastructure.models.orm.user_dao import User
from src.infrastructure.services.db_service import DatabaseService


class UserRepositoryImpl(UserRepository):

    @inject
    def __init__(self, db_service: DatabaseService):
        self.db_service = db_service

    def get_all_users(self):
        return User.query.all()
