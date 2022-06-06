from datetime import date
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from requests import request
from app.downloader import Downloader
from typing import Optional
from pathlib import Path
import pandas as pd

# Initializing the application
app = FastAPI()

# setting the path for static files (for css files)
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)

# setting the path for templates (for html files)
templates = Jinja2Templates(directory="templates")

# get request to load the start page where the user can insert the desired dates
@app.get("/")
async def get_dates(request: Request):
    data = ""
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


# post method to retrieve the user input and make the request to the NASA api 
@app.post("/")
async def get_data(request: Request, start_date: date = Form(default=""), end_date: Optional[date] = Form(default="")):
    # for both 'start' and 'end' dates we set the default value to an empty string, as it is easy to catch errors

    # check if the user inserted a value for the 'start date'
    if start_date == "":
        # if the user does not set a 'start date' we use as 'start date' the current date and as an 'end date' an empty string
        # if the api does not find an 'end date', it sets the 'end date' for seven days after the 'start date'

        today = date.today()
        start_date = today.strftime("%Y-%m-%d")
        end_date = ""

        # create an object of Downloader class
        # and pass the values
        dl = Downloader()
        data = dl.fetch_asteroids(start_date=start_date, end_date=end_date)
        print(data)

        # check if the Downloader class returns a dataframe with the desired objects, or not
        if isinstance(data, pd.DataFrame):
            # if the Downloader returns a dataframe, meaning the desired objects, we return it as an html table
            return templates.TemplateResponse("page.html", {"request": request, "data": data.to_html(index=False, justify="center")})
        else:
            # if it is not, we return a message that no objects were found
            data = "0 objects found."
            return templates.TemplateResponse("page.html", {"request": request, "data": data})

    # after checking for the 'start date', we check again for the 'end date'
    elif end_date == "":
        # if the api does not find an 'end date', it sets the 'end date' for seven days after the 'start date'
        # so we do not change the value of the 'end date'

        start_date = start_date.strftime("%Y-%m-%d")

        # create an object of Downloader class
        # and pass the values
        dl = Downloader()
        data = dl.fetch_asteroids(start_date=start_date, end_date=end_date)
        print(data)

        # check if the Downloader class returns a dataframe with the desired objects, or not
        if isinstance(data, pd.DataFrame):
            # if the Downloader returns a dataframe, meaning the desired objects, we return it as an html table
            return templates.TemplateResponse("page.html", {"request": request, "data": data.to_html(index=False, justify="center")})
        else:
            # if it is not, we return a message that no objects were found
            data = "0 objects found."
            return templates.TemplateResponse("page.html", {"request": request, "data": data})
    else:
        # if the user correctly inserted both 'start' and 'end date', then we pass these values to the Downloader to make the request to the api

        start_date = start_date.strftime("%Y-%m-%d")
        end_date = end_date.strftime("%Y-%m-%d")

        # create an object of Downloader class
        # and pass the values
        dl = Downloader()
        data = dl.fetch_asteroids(start_date=start_date, end_date=end_date)
        print(data)
        
        # check if the Downloader class returns a dataframe with the desired objects, or not
        if isinstance(data, pd.DataFrame):
            # if the Downloader returns a dataframe, meaning the desired objects, we return it as an html table
            return templates.TemplateResponse("page.html", {"request": request, "data": data.to_html(index=False, justify="center")})
        else:
            # if it is not, we return a message that no objects were found
            data = "0 objects found."
            return templates.TemplateResponse("page.html", {"request": request, "data": data})


