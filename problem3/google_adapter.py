from datetime import datetime
import googlemaps
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GoogleAdapter():
    IMPERIAL_UNITS = 'imperial'
    METRIC_UNITS = 'metric'
    DRIVING_MODE = 'driving'
    METERS_IN_MILES = 1609.34
    SEC_IN_MIN = 60

    def __init__(self, api_key):

        self.client = googlemaps.Client(key=api_key)

    def _meters_to_miles(self, meters):
        return round(meters / self.METERS_IN_MILES, 1)

    def _seconds_to_minutes(self, seconds):
        return seconds / self.SEC_IN_MIN

    def route_estimate(self, origin, destination, departure_time=None):

        departure_time = departure_time if departure_time else datetime.now()

        resp = self.client.distance_matrix(
            origins=origin,
            destinations=destination,
            departure_time=departure_time,
            mode=self.DRIVING_MODE,
            units=self.IMPERIAL_UNITS
        )

        elements = resp['rows'][0]['elements'][0]

        distance = self._meters_to_miles(elements["distance"]["value"])
        time = self._seconds_to_minutes(elements["duration"]["value"])

        return (distance, time)











