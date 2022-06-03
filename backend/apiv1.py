
from flask import Blueprint
from flask_restx import Api
from apis.routes_namespace import routes_ns
from apis.gmto_namespace import gmto_ns

blueprint = Blueprint('api', __name__, url_prefix='/')
api = Api(blueprint, version='1.0', title="'Millennium Falcon Challenge' API",
          description='An API to get the probability of success of \
              the Falcon\'s mission as a number ranging from 0 to 100.')

api.add_namespace(routes_ns)
api.add_namespace(gmto_ns)
