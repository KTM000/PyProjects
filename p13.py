########## live weather notification ########

from plyer import notification
import requests


city = "Bremen"
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = {"name": city, "count": 1}
geo_resp = requests.get(geo_url, params=geo_params)

if geo_resp.json()["results"]:
    lat = geo_resp.json()["results"][0]["latitude"]
    long = geo_resp.json()["results"][0]["longitude"]

    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude":lat,
        "longitude": long,
        "current_weather": True
    }
    weather_resp = requests.get(weather_url, weather_params)

    if weather_resp.json()["current_weather"]:
        temp = weather_resp.json()["current_weather"]["temperature"]
        wind = weather_resp.json()["current_weather"]["windspeed"]

        weather_info = (f"Ville:{city}\n"
                        f"1-Temperature:{temp}{weather_resp.json()["current_weather_units"]["temperature"]}\n"
                        f"2-Vent:{wind}{weather_resp.json()["current_weather_units"]["windspeed"]}")

        notification.notify(
            title="Weather Update",
            message= weather_info,
            timeout= 5
        )

    else:
        print("Donnees non trouvees!")
else:
    print("Ville non trouvee!")