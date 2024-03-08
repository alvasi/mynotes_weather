from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY")
BASE_URL = "http://api.weatherstack.com/"


@app.route("/current_weather", methods=["GET"])
def current_weather():
    city = request.args.get("city")
    response = requests.get(f"{BASE_URL}current?access_key={API_KEY}&query={city}")
    if not response.ok:
        return None, "Error fetching weather data"
    weather_data = response.json()
    temperature = weather_data["current"]["temperature"]
    weather_description = (
        weather_data["current"]["weather_descriptions"][0]
        if weather_data["current"]["weather_descriptions"]
        else "Description not available"
    )
    return jsonify(temperature=temperature, weather_description=weather_description)


# @app.route("/forecast", methods=["GET"])
# def forecast():
#     city = request.args.get("city")
#     days = request.args.get("days")
#     response = requests.get(f"{BASE_URL}forecast?access_key={API_KEY}&query={city}&forecast_days={days}&hourly=0")
#     if not response.ok:
#         return None, "Error fetching weather data"
#     weather_data = response.json()
#     return jsonify(weather_data)


if __name__ == "__main__":
    app.run(debug=True)
