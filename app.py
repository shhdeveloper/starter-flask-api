from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')

def hello_world():
    # Create an example list
    my_list = ["String 1", "String 2", "String 3"]

    # Return the list as a JSON response
    return jsonify(my_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    


