from flask import Flask
from flask_cors import CORS
from apiv1 import blueprint as apiv1


# ----------- APP SETUP ----------- #

app = Flask(__name__)
cors = CORS(app, resources={r"/give-me-the-odds/*": {"origins": "*"}})
app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
app.config['RESTX_MASK_SWAGGER'] = False
app.register_blueprint(apiv1)

# ----------- RUNNING THE APP ----------- #


if __name__ == '__main__':
    app.run(debug=True)
