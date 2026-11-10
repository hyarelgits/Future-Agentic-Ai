# import FastAPI framework
from fastapi import FastAPI

# create FastAPI application object
app = FastAPI()

# create GET API endpoint
@app.get("/")

# function runs when route is called
def home():

    # return JSON response
    return {
        "message": "SRE Copilot Running"
    }

