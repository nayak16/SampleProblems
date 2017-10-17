import googlemaps


class GoogleAdapter():

    def __init__(self, api_key):

        self.client = googlemaps.Client(key=api_key)
