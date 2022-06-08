from flask_restx import Namespace, Resource, fields
from functions.gmto_functions import compute_odds

# ----------- API ----------- #

gmto_ns = Namespace('give-me-the-odds', 'Give Me The Odds API')

# ----------- FIELDS ----------- #

odds_fields = gmto_ns.model('Odds', {
    'odds': fields.Float
})

parser = gmto_ns.parser()
parser.add_argument('millennium-falcon')
parser.add_argument('empire', required=True)


@gmto_ns.route('/')
@gmto_ns.expect(parser)
class Odds(Resource):
    """Shows the computed odds."""
    @gmto_ns.marshal_with(odds_fields)
    @gmto_ns.response(200, 'Success')
    @gmto_ns.doc(params={
        'millennium-falcon': {
            'description': 'The `millennium-falcon.json` file relative to `backend/`. \
                If not provided, it uses the default one stored in `backend/`.',
            'type': 'string'
        },
        'empire': {
            'description': 'The `empire.json` file relative to `backend/`.',
            'type': 'string'
        }
    }
    )
    def get(self):
        """Computed odds."""
        args = parser.parse_args()
        empire_path = args['empire']
        if (args['millennium-falcon'] is not None):
            odds = compute_odds(
                empire_path, millennium_falcon_file=args['millennium-falcon'])
        else:
            odds = compute_odds(empire_path)

        return {'odds': odds}
