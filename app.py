from flask import Flask, request, render_template
import requests

app = Flask(__name__)

def get_geolocation(ip):
    response = requests.get(f"http://ip-api.com/json/{ip}")
    return response.json()

@app.route('/')
def index():
    ip = request.remote_addr  # Capture the IP address of the visitor
    location_data = get_geolocation(ip)  # Get location data
    return render_template('map.html', data=location_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
