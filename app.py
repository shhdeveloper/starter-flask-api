from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Create an empty list
    my_list = []

    # Add string data to the list
    my_list.append("String 1")

    # Return the list as a JSON response
    return jsonify(my_list)

@app.route('/')
def list():

    # Create an empty list
    my_list = []

    # Add string data to the list
    my_list.append("String 1")

    # Print the list
    print(my_list)

    return 'Hello'