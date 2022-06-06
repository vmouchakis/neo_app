# This is a simple application to fetch the nearest objects to aerth for a specific date range using the [NASA api](https://api.nasa.gov/). 
# To do this we used **Fastapi**, **Virtualenv** and **Pip3**.

## Download and install the app

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
- If we do not choose a starting date, then the application assumes as starting date the current date and as an ending date an empty string. If the api does not find an ending date, it sets the ending for seven days after the starting date.
- If the user correctly inputs a starting date but not an ending date, the api sets the ending for seven days after the starting date.
- If the user correctly inputs both starting and ending dates, we check if the difference between them is more than 7 days or less than 0 days.
    - If so, we set as starting date the value that the user initially inserted and as ending date en empty string. 
    - If not, we pass both values that the user inserted.

Below is an example of how the results will be shown:
 ![Results](/images/results.jpeg)