from src.infrastructure.services.db_service_impl import db_orm


class User(db_orm.Model):
    id = db_orm.Column(db_orm.Integer, primary_key=True)
    username = db_orm.Column(db_orm.String(80), unique=True, nullable=False)
    email = db_orm.Column(db_orm.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
