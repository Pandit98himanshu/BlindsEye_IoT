#Credits : https://www.thepythoncode.com/article/get-geolocation-in-python

from geopy.geocoders import Nominatim
import time
import geocoder

#Instantiate a new Nominatim client
app = Nominatim(user_agent="BlindsEye")

def get_address(language="en"):
    #Get your coordinates
    g=geocoder.ip('me')
    latitude=g.lat
    longitude=g.lng
    #Build coordinates string to pass to reverse() function
    coordinates = f"{latitude}, {longitude}"
    try:
        return app.reverse(coordinates, language=language).raw
    except:
        return get_address_by_location(latitude, longitude)

