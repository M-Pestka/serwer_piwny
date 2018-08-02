import grequests

default_places = [
    grequests.get("http://nextbike.net/maps/nextbike-official.xml?place=2585728"),
    grequests.get("http://nextbike.net/maps/nextbike-official.xml?place=2586272"),
    grequests.get("http://nextbike.net/maps/nextbike-official.xml?place=2585724"),
    grequests.get("http://nextbike.net/maps/nextbike-official.xml?place=2585779"),
    grequests.get("http://nextbike.net/maps/nextbike-official.xml?place=2585766"),
    grequests.get("http://nextbike.net/maps/nextbike-official.xml?place=2586729"),
    grequests.get("http://nextbike.net/maps/nextbike-official.xml?place=2585731"),
    grequests.get("http://nextbike.net/maps/nextbike-official.xml?place=2675985")
]

def handle():
    responses = grequests.map(default_places)
    texts = [response.text for response in responses]
    return texts[0]

    