from flask_restplus import Namespace, Resource
from flask import jsonify

api = Namespace('password', description='Generate password endpoints')


@api.route('/')
class Password(Resource):
    @api.doc("Generator Request")
    def get(self):
        return jsonify(message="API Generator Password")
