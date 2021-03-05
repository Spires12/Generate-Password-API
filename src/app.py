from flask import Flask
from extension.router_extension import register_routes

def create_app():
  """ 
  Function created app in project 
  
  """

  app = Flask(__name__)
  app.config['ERROR_404_HELP'] = False
  register_routes(app)  
  return app
  