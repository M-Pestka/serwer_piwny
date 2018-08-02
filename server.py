from flask import Flask
import codecs

b_server = Flask(__name__)

@b_server.route("/api-docs")
def api_docs():
    filename = 'public/api_docs.html'
    with codecs.open(filename,'r', encoding='utf8') as file:
        page = file.read()
    return str(page)

b_server.run()