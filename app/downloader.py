import requests
import pandas as pd
pd.set_option('display.float_format', '{:.8f}'.format)
from collections import defaultdict


class Downloader():

    # create a method to send a request to the api, retrieve and manipulate the response, and show the results
    def fetch_asteroids(self, start_date, end_date):

        # initializing the appropriate  parameters for the request
        # the 'url' and its parapemeters were retrieved from the documentation of the NASA api
        # as parameters we need the 'start' and 'end date' and the 'api key'
        # the 'detailed' parameter is optional and it enables a more detailed response from the api
        url = "https://api.nasa.gov/neo/rest/v1/feed"
        params = {
            "api_key":"DpmLXIe2jzwffE2vxsZcEp8ye0rwpiddSJrJvonu",
            "start_date":start_date,
            "end_date":end_date,
            "detailed":"true"
        }
        response = requests.get(url,params=params).json()

        # check if the api found at least one object
        # if not, we return '0' (we 'll check if this class returns a datframe or not)
        # this mostly happens when we choose extreme dates, eg. 2567 or 565
        if response["element_count"]  == 0:
            return 0

        # save the objects in a list for easier manipulation
        neo = response["near_earth_objects"]

        # saving the dates in a list (dates are specified from the user)
        dates = []
        for date in neo:
            dates.append(date)

        # create a temp list to save the objects of each date
        asteroids_temp = []
        for date in dates:
            
            for asteroid in neo[date]:
                asteroids_temp.append(asteroid)

        # create a dict to save the desired attributes for each object
        asteroids = defaultdict(dict)
        for asteroid in asteroids_temp:
            # for each object we save its id, its name, it's closets distance to earth in km, the date of its closest distance to earth
            # and its size, to calculate its size, we find the mean of its max and min diameters in km, as the objects usually don't have a spherical shape
            asteroids[asteroid["id"]] = {"name": [], "approach_distance (km)": [], "approach_date": [], "size (km)": []}
            asteroids[asteroid["id"]]["name"] = asteroid["name"]
            asteroids[asteroid["id"]]["size (km)"] = (asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_max"] + asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_min"]) / 2
            asteroids[asteroid["id"]]["approach_date"] = asteroid["close_approach_data"][0]["close_approach_date"]
            asteroids[asteroid["id"]]["approach_distance (km)"] = asteroid["close_approach_data"][0]["miss_distance"]["kilometers"]
            

        # create a dataframe out of the previous dict and sort values by the 'approach distance' ascending
        df = pd.DataFrame.from_dict(asteroids).T
        df["approach_distance (km)"] = df["approach_distance (km)"].astype(float)
        df.sort_values(by=["approach_distance (km)"], inplace=True)
        return df