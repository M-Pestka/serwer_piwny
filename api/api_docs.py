import codecs
import os 

filename = os.getcwd() + '/public/api_docs.html'

def handle():

    with codecs.open(filename,'r', encoding='utf8') as file:
        page = file.read()
    return str(page)