import grequests
from flask import Response, jsonify
import xmltodict
import json
import re 

default_places = [
    grequests.get("https://nextbike.net/maps/nextbike-official.xml?place=2585728"),
    grequests.get("https://nextbike.net/maps/nextbike-official.xml?place=2585724"),
    grequests.get("https://nextbike.net/maps/nextbike-official.xml?place=2586272"),
    grequests.get("https://nextbike.net/maps/nextbike-official.xml?place=2585779"),
    grequests.get("https://nextbike.net/maps/nextbike-official.xml?place=2585766"),
    grequests.get("https://nextbike.net/maps/nextbike-official.xml?place=2585729"),
    grequests.get("https://nextbike.net/maps/nextbike-official.xml?place=2585731"),
    grequests.get("https://nextbike.net/maps/nextbike-official.xml?place=2585735"),
    grequests.get("https://nextbike.net/maps/nextbike-official.xml?place=2675985")
]

def handle():
    responses = grequests.map(default_places)
    places_info = [(xmltodict.parse(response.text))['markers']['country'][0]['city']['place'] for response in responses]
    processed_places_info = []
    for place_info in places_info:
        has_tandem = False
        available_types = re.findall(r'"(.*?)"', place_info['@bike_types'])
        for bicycle_type in available_types:
            if bicycle_type == "51":
                has_tandem = True
        processed_places_info.append({
            "name": str(place_info['@name']),
            "bikes": int(place_info['@bikes']),
            "bike_racks": int(place_info['@bike_racks']),
            "tandem": str(has_tandem)
        })
    
    return Response(json.dumps(processed_places_info, ensure_ascii=False), mimetype='application/json')

    