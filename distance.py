from geopy.geocoders import Nominatim

from geopy.distance import geodesic

def distance_between_nbo_cairo():
    '''
    Python program to find the distance between Nairobi and Cairo
    using the Nominatim API and GeoPy package
    '''
    # Nairobi
    geolocator = Nominatim(user_agent="skae-application")
    location = geolocator.geocode('Nairobi')
    nairobi = (location.latitude, location.longitude)

    # Cairo
    location = geolocator.geocode("Cairo")
    cairo = (location.latitude, location.longitude)

    # Calculate the distance between the two points
    distance = geodesic(nairobi, cairo).km
    print(f"The distance between Nairobi and Cairo is {distance}km")

#invoking the function
distance_between_nbo_cairo()