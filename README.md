This is a simple application to fetch the nearest objects to aerth for a specific date range using the NASA api.
To do this we used Fastapi, Virtualenv and Pip3.

To use this application please copy and paste the following commands:
```
# copy the repo locally
git clone https://github.com/vmouchakis/neo_app.git

# go to the directory of the app
cd neo_app

# create a virtual environment (called venv) to install the required python packages
virtualenv venv

# activate the virtual environment
source venv/bin/activate

# install the required python packages
pip3 install -r requirements.txt
```

To run the application copy the following command
```
uvicorn app.main:app
```

The application will run on the following [link](http://localhost:8000/).

This is the starting page of the application

 ![Starting page](/images/start-page.jpeg)

Here we can choose the time interval.
If we do not choose a starting date, then the application assumes as starting date the current date and as an ending date 