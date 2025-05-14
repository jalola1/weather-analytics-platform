from flask import Flask, request, jsonify

app = Flask(__name__) #initialize Flask app

@app.route("/") #route for home page
def home():
    return "Welcome to the Weather API!"

@app.route("/weather") #route for weather data
def get_weather():
    #Return mock weather data
    return jsonify({
        "location": "New York",
        "temperature": 70,
        "conditions": "Sunny"
    })

if __name__ == "__main__": 
    print("Available routes: ")
    print(app.url_map)
    app.run(host='0.0.0.0', port=5000, debug=True)


