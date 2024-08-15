from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '162f203e4329d0df88adde0ff2b2e712'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('map.html')

@socketio.on('send-location')
def handle_location(data):
    socketio.emit('receive-location', data)

@socketio.on('disconnect')
def handle_disconnect():
    socketio.emit('user-disconnected', request.sid)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
