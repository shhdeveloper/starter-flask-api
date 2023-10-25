from flask import Flask, jsonify, render_template, request
import os

app = Flask(__name__)

my_list = []  # Initialize a list to store data

@app.route('/add_data', methods=['POST'])
def add_data():
    data = request.get_json()  # Assuming you send JSON data in the request

    if 'data' in data:
        new_data = data['data']
        my_list.append(new_data)
        return jsonify({"message": "Data added successfully"})
    else:
        return jsonify({"error": "Invalid data format"}), 400 
    

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify({"data": my_list})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    