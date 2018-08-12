from flask import Response
import json

def handle_get_owed_beers(db, id):
    try:
        beers = db.get_piwka_ktore_wisisz(id)
        logins = [el[1] for el in beers]
        unique_logins = set(logins)
        response = []
        while True:
            try:
                login = unique_logins.pop()
                how_much = logins.count(login)
                result = {
                    "login": login,
                    "quantity": how_much
                }
                response.append(result)
            except Exception:
                break

        response = {
            "owed_beers": response,
            "error": False
        }
        return Response(json.dumps(response, ensure_ascii=False), mimetype='application/json')
    
    except Exception:
        return Response(json.dumps({"error": True}, ensure_ascii=False), mimetype='application/json')
