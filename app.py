import asyncio
from flask import Flask, jsonify, render_template, request
import os
import subprocess
from ping3 import ping, verbose_ping

# Define the host or IP address you want to ping



app = Flask(__name__)

my_list = []  # Initialize a list to store data

async def ping_host(host):
    try:
        ping_time = ping(host)
        return ping_time
    except subprocess.CalledProcessError:
        return "Ping failed. The host may be unreachable."

@app.route('/add_data', methods=['POST'])
def add_data():
    host = "cyclic.sh"  # Change this to the desired host
    data = request.get_json()  # Assuming you send JSON data in the request

    if 'data' in data:
        new_data = data['data']

        # Asynchronously ping the host
        ping_result = asyncio.run(ping_host(host))

        my_list.append({"data": new_data})
        return jsonify({"message": "Data added successfully", "ping": ping_result})
    else:
        return jsonify({"error": "Invalid data format", "ping": ping_result}), 400

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify({"data": my_list})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    