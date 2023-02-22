from fast import FastAPI

WEATHER = {
    "london": "rainy",
    "paris": "sunny",
}


def get_current_weather(city = "london"):
    return WEATHER.get (city,"storm")

app = FastAPI()

@app.get("/weather")
def weather(city: str)-> dict:
    return {"weather": get_current_weather() }

WEATHER = {
    "london": "rainy",
    "paris": "sunny",  
}

def get_current_weather(city):
    return WEATHER.get (city, "storm")

app = FastAPI()

@app.get("/weather")
def weather(city: str = "london")-> dict:
    return {"weather": get_current_weather() }

    
    
    
              