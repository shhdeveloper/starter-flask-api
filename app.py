from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Initialize a list to store the data
my_list = []

@app.route('/')
def hello_world():
    # Return the list as a JSON response
    return jsonify(my_list)

@app.route('/add_data', methods=['POST'])
def add_data():
    # Retrieve data from the form
    new_data = request.form.get('data')

    # Append the new data to the list
    my_list.append(new_data)

    # Redirect to the main page or you can return a response
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
