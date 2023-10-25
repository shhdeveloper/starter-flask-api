from flask import Flask, render_template, request, jsonify

import requests

url = "https://dark-pink-indri-yoke.cyclic.app/add"

response = requests.get(url)

if response.status_code == 200:
    print("Response from", url, ":", response.text)
else:
    print("Failed to retrieve data from", url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
