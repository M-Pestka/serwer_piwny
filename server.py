from flask import Flask, Response, request
from api import api_docs, bicycles, beers
from flask_cors import CORS
import os
import json
import create_db
import Db

b_server = Flask(__name__)
CORS(b_server)
create_db.initialize()
db = Db.Piwna_baza()

@b_server.route("/api-docs")
def api_docs_handler():
    return api_docs.handle()


@b_server.route("/bicycles")
def bicycle_handler():
    return bicycles.handle()

@b_server.route("/logins")
def users_handler():
    users = db.get_all_users()
    logins = []
    for user in users:
        logins.append(user[0])
    return Response(json.dumps({"all_users": logins}, ensure_ascii=False), mimetype='application/json')
    
@b_server.route("/beers/loaner")
def get_owed_beers():
    id = request.args.get('id')
    return beers.handle_get_owed_beers(db, int(id))

@b_server.route("/beers/lender")
def get_lent_beers():
    id = request.args.get('id')
    return beers.handle_get_lent_beers(db, int(id))

b_server.config['RESTFUL_JSON'] = {
        'ensure_ascii': False
}



port = int(os.environ.get('PORT', 5000))
b_server.run(host='0.0.0.0', port=port)
