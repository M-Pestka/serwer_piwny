import grequests
from flask import Response, jsonify
import xmltodict
import pprint
import json

default_places = [
    grequests.get("http://nextbike.net/maps/nextbike-official.xml?place=2585728"),
    grequests.get("http://nextbike.net/maps/nextbike-official.xml?place=2585724"),
    grequests.get("http://nextbike.net/maps/nextbike-official.xml?place=2586272"),
    grequests.get("http://nextbike.net/maps/nextbike-official.xml?place=2585779"),
    grequests.get("http://nextbike.net/maps/nextbike-official.xml?place=2585766"),
    grequests.get("http://nextbike.net/maps/nextbike-official.xml?place=2585729"),
    grequests.get("http://nextbike.net/maps/nextbike-official.xml?place=2585731"),
    grequests.get("http://nextbike.net/maps/nextbike-official.xml?place=2585735"),
    grequests.get("http://nextbike.net/maps/nextbike-official.xml?place=2675985")
]

def handle():
    pp = pprint.PrettyPrinter(indent=2)
    responses = grequests.map(default_places)
    places_info = [(xmltodict.parse(response.text))['markers']['country']['city']['place'] for response in responses]
    processed_places_info = []
    for place_info in places_info:
        processed_places_info.append({
            "name": str(place_info['@name']),
            "bikes": int(place_info['@bikes']),
            "bike_racks": int(place_info['@bike_racks'])
        })
    
    return Response(json.dumps(processed_places_info, ensure_ascii=False), mimetype='application/json')

    