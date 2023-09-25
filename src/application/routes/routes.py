from src.application.routes.hello_routes import hello_routes
from src.application.routes.orchestrator_routes import orchestrator_routes


def register_routes(app):
    app.register_blueprint(hello_routes)
    app.register_blueprint(orchestrator_routes)

