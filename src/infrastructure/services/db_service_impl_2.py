from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from typing import Optional

import config
from src.infrastructure.models.orm.user_dao import User
from src.infrastructure.services.db_service import DatabaseService

db_orm = SQLAlchemy()


class DatabaseServiceImpl2(DatabaseService):
    def __init__(self, app: Flask,
                 user: str,
                 password: str,
                 host: str,
                 port: int,
                 dbname: str,
                 track_modifications: bool = True):
        """Initialize the database service with the given app and configurations.

        :param app: Flask app instance.
        :param user: Database user.
        :param password: Database password.
        :param host: Database host.
        :param port: Database port.
        :param dbname: Database name.
        :param track_modifications: SQLAlchemy track modifications setting.
        """

        app.config['SQLALCHEMY_DATABASE_URI'] = (f"mysql"
                                                 f"://{config.DB_USER}"
                                                 f":{config.DB_PASSWORD}"
                                                 f"@{config.DB_HOST}"
                                                 f"/{config.DB_NAME}")

        db_uri = f"mysql://{user}:{password}@{host}:{port}/{dbname}"
        app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI']
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = track_modifications

        try:
            self.db_orm = db_orm
            self.db_orm.init_app(app)
        except Exception as e:
            # For a production application, more specific exceptions and error handling would be needed.
            raise RuntimeError(f"Error initializing database service: {str(e)}")

    def get_db(self) -> Optional[SQLAlchemy]:
        """Retrieve the initialized SQLAlchemy instance.

        :return: SQLAlchemy instance if initialized, else None.
        """
        return self.db_orm

    def get_all_users(self):
        return User.query.all()

    @classmethod
    def from_uri(cls, app: Flask, db_uri: str, track_modifications: bool = True):
        app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = track_modifications
        return cls(app, "", "", "", 0, "")  # Passing default values to the __init__ method
