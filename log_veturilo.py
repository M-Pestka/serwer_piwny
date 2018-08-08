import requests
import xmltodict
import json
import time


def zgarnij_dane() -> dict:
    dane = requests.get('http://nextbike.net/maps/nextbike-official.xml?city=210')
    dane = xmltodict.parse(dane.text)
    dane = dane['markers']['country']['city']['place']
    
    wynik = {'dzisiejsza data': time.time() }  
    lista_miejsc = []
    for place in dane:
        
        if(int(place['@bikes']) >= 2):
            lista_row = [int(x) for x in place['@bike_numbers'][1:-1].split(',')]
        elif(int(place['@bikes']) == 1):
            lista_row = [int(place['@bike_numbers'])]
        else:
            lista_row = []
            
        lista_miejsc.append({'uid': int(place['@uid']),
                                'bike_numbers': lista_row,
                                'bike_types': place['@bike_types']})
        
    
    wynik['places'] = lista_miejsc
    with open('chuj_{}.json'.format(str(time.time()).split('.')[0]), 'w') as p:
        json.dump(wynik, p)

def sciagaj_co_10_minut():
    while 1:
        zgarnij_dane()
        print('dane pobrane i zapisane')
        time.sleep(600)


if(__name__ == '__main__'):
    sciagaj_co_10_minut()



