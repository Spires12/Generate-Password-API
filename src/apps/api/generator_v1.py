from flask import Blueprint
from flask_restplus import Api 
from .generator.controller.generator_password import api as password_api
from werkzeug.exceptions import HTTPException

blueprint = Blueprint('generator_api', __name__, url_prefix='/generator' )

api = Api(blueprint,
          doc='/doc/',
          title='Resource API - Generator',
          version='1.0.0',
          description='Gereated code'
          )

api.add_namespace(password_api)

@api.errorhandler(HTTPException)
def handle_error(error: HTTPException):
  """ Handle Blueprint Json Error Response """
  response = {
    'error': error.__class__.__name__,
    'message': error.description,
  }
  return response, error.code

    
