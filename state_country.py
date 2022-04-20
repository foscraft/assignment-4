from geopy.geocoders import Nominatim

def coordinate_details(latitude, longitude):
    '''
    Python function to get the city, state and country name of a specified
    latitude and longitude using Nominatim API and Geopy package
    '''
   
    geolocator = Nominatim(user_agent="skae-application")
    location = geolocator.reverse(f"{latitude}, {longitude}")
    return location.address

#invoking the function
# Nairobi
print(coordinate_details(-1.28333, 36.81667))