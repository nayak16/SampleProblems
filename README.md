# Aatish Open Listings Interview

To run any of the solution code, activate the python virtual environment:
```
source env/bin/activate
```

## Problem 1

Run `python problem1/main.py` to run the test suite.
The runtime efficiency of the `get_dim` function is discussed under the function definition


## Problem 2

Run the following code to find all the html files with the domain 'shittylistings.com':
```
python problem2/main.py
```
The script uses `problem2/website` as the root directory and this is the file structure. Each file marked with `*` has a link to the domain 'shittylistings.com':
```
website
|
+--- index.html*
+--- about.html*
+--- [san-dego]
|       +--- 2505-via-clarita.html
|
+--- [los-angeles]
        +--- culver-city.html*
        +--- [marina]
                +--- listings.html
```

In the file `html_scraper.py` I use a subclass of a Python HTML parser library to extract all the link tags from each file and filter for ones that have the target domain. At the minimum, we still have to traverse all files to check it's links. Thus, the runtime is O(n). However, even with 50k files, if the root directory is properly specified, the task will easily finish within 24 hours.


## Problem 3
The core logic of the route estimator is in the `google_adapter.py` file. The main `route_estimate` function returns a distance in miles and time in minutes. To test out the estimator run the following with addresses of your choice. 
Example:
```
python problem3/route_estimate.py -o "8535 Hargis Street, Los Angeles, CA" -d "1720 Pacific Ave, Venice, CA 90291" -t "19:00"
```
For usage instructions run `python route_estimate.py --help`.

The CLI sets the departure time to the closest in the future. For example if it's currently 10/18/17 9:00 am, and you choose 10:00 as the time, it will set the date to 10/18/17 10:00 am. If you choose 8:00, it will set the date to 10/19/17 8:00. 

### Further Improvements
The Google Distance Matrix API has a lot of extremely powerful features. Here are a few features I would add in this scenario:

1. The API supports passing in multiple origin and destination addresses and returns the route estimates for each pairing in the cross product, hence the matrix name. This is especially useful when creating a dispatch system for on-demand showings to agents. You can have multiple showing addresses (destinations) and current locations for agents (origins) and calculate the time and distance for each pairing. This would allow the system to intelligently dispatch a request for a showing to the agent who's closest using time and distance. I would encapsulate this functionality in a function called `multiple_route_estimates`.
2. The API also supports different traffic models for the routing estimate: best guess, optimistic, and pessimistic. With a city like LA, it would be preferable to use a pessimistic option. This would allow for more precise dispatching and accurate ETAs. 
3. Additionally, instead of departure time, we can provide the desired arrival time, when the agent should get to the showing, to the API to get the ETA. Comparing it to historic data, we can determine which time estimate, departure or arrival, can determine better ETAs
4. In the case the agents are using public transportation, the Maps API also provides a way to estimate the time and distance to a destination using bus, rail, or subway.
5. For argument checking and client usage flexibility, the `route_estimate` function can be modified to take also accept a coordinate pair or geojson instead of just the address string. 