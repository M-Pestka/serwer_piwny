from flask import Flask
from api import api_docs, bicycles

b_server = Flask(__name__)

@b_server.route("/api-docs")
def api_docs_handler():
    return api_docs.handle()


@b_server.route("/bicycles")
def bicycle_handler():
    return bicycles.handle()


b_server.run()