from flask import Flask
from api import api_docs

b_server = Flask(__name__)

@b_server.route("/api-docs")
def api_docs_handler():
    return api_docs.handle()


@b_server.route("/bicycles")
def bicycle_handler():
    return 'strona w budowie'


b_server.run()