from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Create an empty list
    my_list = []

    # Add string data to the list
    my_list.append("String 1")

    # Print the list in the server logs
    print(my_list)

    return "List printed in the server logs"

@app.route('/')
def list():

    # Create an empty list
    my_list = []

    # Add string data to the list
    my_list.append("String 1")

    # Print the list
    print(my_list)

    return 'Hello'