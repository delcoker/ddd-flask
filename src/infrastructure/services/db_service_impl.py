from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.infrastructure.services.db_service import DatabaseService

colours = {
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'reset': '\033[0m'
}
db_orm = SQLAlchemy()


class DatabaseServiceImpl(DatabaseService):

    def __init__(self, flask_app):
        try:
            self.db_orm = db_orm
            self.db_orm.init_app(flask_app)
        except Exception as e:
            print(colours['cyan'] + f"Error initializing database service: {str(e)}" + colours['cyan'])
            # For a production application, more specific exceptions and error handling would be needed.
            # raise RuntimeError(f"Error initializing database service: {str(e)}")

    def get_db(self):
        """Retrieve the initialized SQLAlchemy instance.

        :return: SQLAlchemy instance if initialized, else None.
        """
        return self.db_orm

    @classmethod
    def from_uri(cls, app: Flask, db_uri: str, track_modifications: bool = True):
        app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = track_modifications
        return cls(app, "", "", "", 0, "")  # Passing default values to the __init__ method
