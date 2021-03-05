from apps.api.generator_v1 import blueprint as generator_v1


def register_routes(app):
  """
  Register router blueprint

  """
  app.register_blueprint(generator_v1)
  