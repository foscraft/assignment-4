from geopy.geocoders import Nominatim



def country_finder(state):
    '''
    Python program to search the country name from a given state name
    using the  Nominatim API and GeoPy package
    '''
    geolocator = Nominatim(user_agent="skae-application")
    location = geolocator.geocode(state)
    return f' The Country name for {state} state is {location.address.split(",")[-1]}'

#invoking the function
print(country_finder("Nairobi"))
    