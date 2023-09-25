from flask import Blueprint, jsonify
from injector import inject

from src.application.services.orchestrator_service import OrchestratorService

route_path = '/orchestrator'
orchestrator_routes = Blueprint('orchestrator', __name__)


@orchestrator_routes.route(f'{route_path}/api', methods=['GET'])
@inject
def get_orchestrator_api(orchestrator_service: OrchestratorService):
    api_data = orchestrator_service.get_api_data()
    return jsonify(api_data), 201


@orchestrator_routes.route(f'{route_path}/functional', methods=['GET'])
@inject
def get_orchestrator_functional(orchestrator_service: OrchestratorService):
    data = orchestrator_service.get_functional_data()
    return jsonify(data), 201


@orchestrator_routes.route(f'{route_path}/db', methods=['GET'])
@inject
def get_orchestrator_db(orchestrator_service: OrchestratorService):
    db_data = orchestrator_service.get_db_data()
    return jsonify(db_data), 200
