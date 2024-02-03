import geocoder
from googletrans import Translator

def location():
    # Getting User Location
    user_location = geocoder.ip('me')
    city = user_location.city

    # Translating (in case)
    translator = Translator()
    translated = translator.translate(city, src='auto', dest='en')
    city = translated.text

    return city

def coordinates():
    ip = geocoder.ip('me')
    lat,lng = ip.lat,ip.lng
    return lat,lng