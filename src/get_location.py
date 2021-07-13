import geocoder
g = geocoder.ip('me')
print(g.lat)
print(g.lng)
