from django.shortcuts import render
import requests
import joblib
import numpy as np
from datetime import datetime

model = joblib.load('models/gradient_boost_model.pkl')

def get_weather_data():
    city = 'Chicago'
    api_key = 'c9c2e98badf69b69f4ee3ed0404c2958'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        temperature = data['main']['temp']
        wind_speed = data['wind']['speed']
        return temperature, wind_speed
    else:
        return None, None

def get_day_type():
    day_of_week = datetime.now().weekday()
    if day_of_week < 5:
        return 0, 0, 1  # Weekday
    elif day_of_week == 5:
        return 1, 0, 0  # Saturday
    else:
        return 0, 1, 0  # Sunday

def index(request):
    temperature, wind_speed = get_weather_data()
    current_month = datetime.now().month
    dy_A, dy_U, dy_W = get_day_type()
    current_date = datetime.now().strftime('%Y-%m-%d')  

    features = np.array([[current_month, temperature, wind_speed, dy_A, dy_U, dy_W]])
    prediction = model.predict(features)[0]
    prediction_result = 'Yes' if prediction == 1 else 'No'

    context = {
        'temperature': temperature,
        'wind_speed': wind_speed,
        'current_month': current_month,
        'day_type': 'A' if dy_A else 'U' if dy_U else 'W',
        'prediction_result': prediction_result,
        'current_date': current_date,  
    }
    return render(request, 'form.html', context)
