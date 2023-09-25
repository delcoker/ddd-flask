from flask import Flask
from flask_injector import FlaskInjector

import config
from container import Container
from src.application.routes import routes


def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object('config')

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = (f"mysql+pymysql"
                                                   f"://{config.DB_USER}"
                                                   f":{config.DB_PASSWORD}"
                                                   f"@{config.DB_HOST}"
                                                   f"/{config.DB_NAME}")

    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS

    return flask_app


app = create_app()
routes.register_routes(app)
container = Container()
FlaskInjector(app=app, modules=[lambda binder: container.configure(binder, app)])

if __name__ == '__main__':
    app.run(debug=config.DEBUG)
