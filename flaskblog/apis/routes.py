
from flask import Blueprint
from flask_restx import Resource, Api

blueprint = Blueprint('api', __name__)
api = Api(
    blueprint,
    version='1.0',
    title='API Title',
    description='Some description',
    default='dog',
    validate=True,
    # ordered= # what this?
    # authorizations= # what this?
    )


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}