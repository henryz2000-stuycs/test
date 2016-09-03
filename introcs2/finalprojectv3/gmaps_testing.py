import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyD7g6o2aIIo3ZlXtYbc4LjhcUaRizS1DKU')

def test():
    now = datetime.now()
    directions_result = gmaps.directions("Times Square, New York", "Stuyvesant High School, New York, NY 10282", mode = "transit", departure_time = now)
    return directions_result
