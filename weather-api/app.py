from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__) #initialize Flask app
API_KEY = os.getenv("OPENWEATHER_API_KEY")

@app.route("/") #route for home page
def home():
    return "Welcome to the Weather API!"

@app.route("/weather") #route for weather data
def get_weather():
    city = request.args.get("city", "New York")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        return jsonify({
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "conditions": data["weather"][0]["description"]
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__": 
    app.run(debug=True)