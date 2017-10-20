import click
from datetime import datetime
from datetime import timedelta
import logging

from google_adapter import GoogleAdapter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Route Estimate CLI")

API_KEY = "AIzaSyDBAjidO8byrVXcY6bR9yqxbhE4HRp_SaU"
TIME_FORMAT = "%H:%M"


def set_up():
    return GoogleAdapter(API_KEY)


@click.command()
@click.option('--origin', '-o', multiple=True,
              help="Origin Address formatted as a string"
                   "Ex: '8535 Hargis Street, Los Angeles, CA'"
              )
@click.option('--destination', '-d', multiple=True,
              help="Destination Address formatted as string"
                   "Ex: '8535 Hargis Street, Los Angeles, CA'"
              )
@click.option('--time', '-t',
              help="Departure time formatted as HH:MM in 24 hour format "
                   "i.e. 16:20. Date defaults to closest in the future. "
                   "If time not specified, defaults to now."
              )
def main(origin, destination, time):

    origin = list(origin)
    destination = list(destination)
    google_adapter = set_up()

    if time:
        try:
            # Set time to closest in the future
            now = datetime.now()
            time = datetime.strptime(time, TIME_FORMAT)
            time = time.replace(
                year=now.year, month=now.month, day=now.day
            )
            if time.time() < now.time():
                time = time + timedelta(days=1)

        except ValueError:
            raise click.BadParameter(
                "Time must be in {} format".format(TIME_FORMAT)
            )

    # Call Google Adapter
    result = google_adapter.route_estimate(
        list(origin), list(destination), departure_time=time
    )

    logger.info(
        "This route will take {} miles and {} minutes".format(
            result['distance'], result['time']
        )
    )


if __name__ == "__main__":
    main()
