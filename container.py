from flask_injector import request
from injector import singleton
from src.application.services.orchestrator_service import OrchestratorService
from src.application.services.orchestrator_service_impl import OrchestratorServiceImpl
from src.domain.repositories.api.api_repository import ApiRepository
from src.domain.repositories.db.user_repository import UserRepository
from src.infrastructure.repositories.api.api_repository_impl import ApiRepositoryImpl
from src.infrastructure.repositories.db.user_repository_impl import UserRepositoryImpl
from src.infrastructure.services.db_service import DatabaseService
from src.infrastructure.services.db_service_impl import DatabaseServiceImpl


class Container:

    @staticmethod
    def configure(binder, flask_app):
        # db2 = DatabaseServiceImpl2(flask_app, config.DB_USER,
        #                            config.DB_PASSWORD,
        #                            config.DB_HOST,
        #                            config.DB_PORT,
        #                            config.DB_NAME)

        binder.bind(DatabaseService, to=DatabaseServiceImpl(flask_app), scope=request)
        binder.bind(UserRepository, to=UserRepositoryImpl, scope=request)
        binder.bind(ApiRepository, to=ApiRepositoryImpl, scope=singleton)
        binder.bind(OrchestratorService, to=OrchestratorServiceImpl, scope=singleton)
        # binder.bind(DatabaseService, to=db2, scope=request)
