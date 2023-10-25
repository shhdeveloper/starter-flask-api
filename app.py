from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!123'
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('message')
def handle_message(data):
    message = data.get('message', '')
    username = data.get('username', '')

    print("Received message from", username, ":", message)
    if message != "User connected!":
        send({'message': message, 'username': username}, broadcast=True)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)