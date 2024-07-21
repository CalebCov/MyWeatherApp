from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)
load_dotenv()
api_key = os.getenv('WEATHER_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    data = request.get_json()
    city = data['city']
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
