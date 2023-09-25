from flask import Blueprint

hello_routes = Blueprint('hello', __name__)


@hello_routes.route('/')
def hello_world():
    return 'Hello Flask!'


@hello_routes.route('/hello/<string:name>/')
def hello_name(name: str):
    return f'Hello {name}!'


@hello_routes.route('/test/<int:number>/')
def hello_number(number: float):
    return f'Hello {number}!'
