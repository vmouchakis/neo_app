from tracemalloc import start
import requests
from pprint import PrettyPrinter
import pandas as pd
pd.set_option('display.float_format', '{:.8f}'.format)
from collections import defaultdict
from datetime import datetime

pp = PrettyPrinter()

api_key = "DpmLXIe2jzwffE2vxsZcEp8ye0rwpiddSJrJvonu"
# start_date = "2020-01-22"
# end_date = "2020-01-24"

class Downloader():

    def fetch_asteroids(self, start_date, end_date):

        # start_date = start_date.strftime("%Y-%m-%d")
        # end_date = end_date.strftime("%Y-%m-%d")

        url = "https://api.nasa.gov/neo/rest/v1/feed"
        params = {
            "api_key":"DpmLXIe2jzwffE2vxsZcEp8ye0rwpiddSJrJvonu",
            "start_date":start_date,
            "end_date":end_date,
            "detailed":"true"
        }
        response = requests.get(url,params=params).json()
        # pp.pprint(response)
        # return response

        # dl = Downloader()
        # data = dl.fetch_asteroids(api_key, start_date, end_date)

        neo = response["near_earth_objects"]

        dates = []

        for date in neo:
            dates.append(date)


        asteroids_temp = []

        for date in dates:
            
            for asteroid in neo[date]:
                asteroids_temp.append(asteroid)


        asteroids = defaultdict(dict)

        for asteroid in asteroids_temp:
            asteroids[asteroid["id"]] = {"name": [], "approach_distance (km)": [], "approach_date": [], "size (km)": []}
            asteroids[asteroid["id"]]["name"] = asteroid["name"]
            asteroids[asteroid["id"]]["approach_distance (km)"] = asteroid["close_approach_data"][0]["miss_distance"]["kilometers"]
            asteroids[asteroid["id"]]["approach_date"] = asteroid["close_approach_data"][0]["close_approach_date"]
            asteroids[asteroid["id"]]["size (km)"] = (asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_max"] + asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_min"]) / 2


        df = pd.DataFrame.from_dict(asteroids).T
        df["approach_distance (km)"] = df["approach_distance (km)"].astype(float)
        df.sort_values(by=["approach_distance (km)"], inplace=True)
        # pp.pprint(df)
        return df.style.hide_index()