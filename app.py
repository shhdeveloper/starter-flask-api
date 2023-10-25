from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def make_get_request():
    url = "https://dark-pink-indri-yoke.cyclic.app/add"
    response = requests.get(url)
    
    if response.status_code == 200:
        response_text = response.text
    else:
        response_text = "Failed to retrieve data from " + url

    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
