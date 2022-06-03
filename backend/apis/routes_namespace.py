from flask_restx import Namespace, Resource, fields

from functions.db_functions import create_connection, select_all_routes

# ----------- API ----------- #

routes_ns = Namespace('routes', 'Routes API')

# ----------- FIELDS ----------- #

routes_fields = routes_ns.model('Route', {
    'origin': fields.String,
    'destination': fields.String,
    'travel_time': fields.Integer
})


@routes_ns.route('/')
class Routes(Resource):
    """Shows a list of all routes."""
    @routes_ns.marshal_with(routes_fields)
    @routes_ns.response(200, 'Success')
    def get(self):
        """List all routes."""
        data = []
        with create_connection('db/universe.db') as cnx:
            for row in select_all_routes(cnx):
                data.append({'origin': row[0],
                             'destination': row[1], 'travel_time': row[2]})
            return data
