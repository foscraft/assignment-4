from geopy.geocoders import Nominatim

def zip_code_details(zip_code):
    '''
    Python program to find the details of a given zip code using the
    Nominatim API and GeoPy package
    '''
    geolocator = Nominatim(user_agent="skae-application")
    location = geolocator.geocode(zip_code)
    return location.address

#invoking the function
print(zip_code_details("90210"))