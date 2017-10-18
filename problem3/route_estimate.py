import click
from datetime import datetime
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
                   "i.e. 16:20. If not specified, defaults to now."
              )
def main(origin, destination, time):

    origin = list(origin)
    destination = list(destination)
    google_adapter = set_up()

    if time:
        try:
            time = datetime.strptime(time, TIME_FORMAT)
        except ValueError:
            raise click.BadParameter(
                "Time must be in {} format".format(TIME_FORMAT)
            )

    logger.info("Calculating time and distance from "
                "{} to {}.".format(origin, destination))

    (dist, time) = google_adapter.route_estimate(
        list(origin), list(destination)
    )

    logger.info(
        "This route will take {} miles and {} minutes".format(dist, time)
    )


if __name__ == "__main__":
    main()
