from flask import Flask
from api import api_docs, bicycles

b_server = Flask(__name__)

@b_server.route("/api-docs")
def api_docs_handler():
    return api_docs.handle()


@b_server.route("/bicycles")
def bicycle_handler():
    return bicycles.handle()


if __name__ == '__main__':
    b_server.config['RESTFUL_JSON'] = {
            'ensure_ascii': False
        }
    b_server.run()