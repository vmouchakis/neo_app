from datetime import date
from pprint import PrettyPrinter
import string
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from requests import request
from app.downloader import Downloader
from datetime import datetime


app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def get_dates(request: Request):
    data = "Test"
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


@app.post("/")
async def get_data(request: Request, start_date: date = Form(...), end_date: date = Form(...)):
    start_date = start_date.strftime("%Y-%m-%d")
    end_date = end_date.strftime("%Y-%m-%d")
    dl = Downloader()
    data = dl.fetch_asteroids(start_date=start_date, end_date=end_date)
    print(data)
    return templates.TemplateResponse("page.html", {"request": request, "data": data.to_html()})



# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request):
#     data = {
#         "page": "Home page"
#     }
#     return templates.TemplateResponse("page.html", {"request": request, "data": data})


# @app.get("/page/{page_name}", response_class=HTMLResponse)
# async def page(request: Request, page_name: str):
#     data = {
#         "page": page_name
#     }
#     return templates.TemplateResponse("page.html", {"request": request, "data": data})