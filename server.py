from flask import Flask
from api import api_docs, bicycles
from flask_cors import CORS
import os

b_server = Flask(__name__)
CORS(b_server)

@b_server.route("/api-docs")
def api_docs_handler():
    return api_docs.handle()


@b_server.route("/bicycles")
def bicycle_handler():
    return bicycles.handle()


b_server.config['RESTFUL_JSON'] = {
        'ensure_ascii': False
}

port = int(os.environ.get('PORT', 5000))
b_server.run()#host='0.0.0.0', port=port)
