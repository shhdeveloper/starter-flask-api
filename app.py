from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

my_list = []  # Initialize a list to store data

@app.route('/')
def index():
    # Render the HTML template
    return render_template('index.html', my_list=my_list)

@app.route('/add', methods=['POST'])
def add_data():
    new_data = request.form.get('data')
    my_list.append(new_data)
    return render_template('index.html', my_list=my_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
