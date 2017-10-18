from datetime import datetime
import googlemaps
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GoogleAdapter():
    __name__ = 'google adapter'

    OK_STATUS = 'OK'
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
        """
        Function that estimates the travel duration and distance between
        two points, given a departure time (defaults to now), by calling the
        Google Distance Matrix API

        :param origin: a string representing an address
        :param destination: a string representing an address
        :param departure_time: the time at which the route is expected to
        start, a datetime object

        :return: the duration (in minutes) that this route will take
        and the distance (in miles) that it is
        """

        departure_time = departure_time if departure_time else datetime.now()

        logger.info("Calculating time and distance from "
                    "{} to {} with departure time {}.".format(
                        origin, destination, departure_time)
                    )
        print(departure_time)
        try:
            resp = self.client.distance_matrix(
                origins=origin,
                destinations=destination,
                departure_time=departure_time,
                mode=self.DRIVING_MODE,
                units=self.IMPERIAL_UNITS
            )
        except Exception as e:
            logger.exception(
                "Google API returned error: {}".format(e)
            )
            return

        status = resp['status']

        if status != self.OK_STATUS or len(resp['rows']) == 0:
            logger.error(
                "Google API returned status {} with no response".format(status)
            )
            return

        elements = resp['rows'][0]['elements'][0]

        distance = self._meters_to_miles(elements["distance"]["value"])
        time = self._seconds_to_minutes(elements["duration"]["value"])

        return {
            "distance": distance,
            "time": time
        }
