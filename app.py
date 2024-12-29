from flask import Flask, render_template, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Simulated sensor data storage
sensor_data = {
    'temperature': 0,
    'humidity': 0,
    'soil_ph': 0,
    'moisture_sensors': [0, 0, 0],
    'is_watering': False
}

MOISTURE_THRESHOLDS = {
    'LOW': 10,
    'HIGH': 40
}

def calculate_moisture_average():
    return sum(sensor_data['moisture_sensors']) / len(sensor_data['moisture_sensors'])

@app.route('/')
def index():
    return render_template('index.html', 
                         sensor_data=sensor_data,
                         moisture_avg=calculate_moisture_average(),
                         thresholds=MOISTURE_THRESHOLDS)

@app.route('/update_sensor', methods=['POST'])
def update_sensor():
    data = request.json
    sensor_type = data.get('type')
    value = float(data.get('value', 0))
    
    if sensor_type in ['temperature', 'humidity', 'soil_ph']:
        sensor_data[sensor_type] = value
    elif sensor_type == 'moisture':
        index = int(data.get('index', 0))
        if 0 <= index < len(sensor_data['moisture_sensors']):
            sensor_data['moisture_sensors'][index] = value
    
    return jsonify({
        'success': True,
        'moisture_avg': calculate_moisture_average()
    })

@app.route('/toggle_watering', methods=['POST'])
def toggle_watering():
    sensor_data['is_watering'] = not sensor_data['is_watering']
    return jsonify({
        'success': True,
        'is_watering': sensor_data['is_watering']
    })

if __name__ == '__main__':
    app.run(debug=True)