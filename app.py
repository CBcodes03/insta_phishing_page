from flask import Flask, request, jsonify, render_template, redirect, url_for
import json

app = Flask(__name__)

# Route to serve the HTML page
@app.route('/', methods=['GET', 'POST'])
def home():
    return redirect(url_for('login'))
   
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user_data = {"email": email, "password": password}
        with open('data.json', 'w') as json_file:
            json.dump(user_data, json_file)
        return redirect(url_for('login'))	

# Route to view stored data
@app.route('/view-data', methods=['GET'])
def view_data():
    try:
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"message": "No data found"})

if __name__ == '__main__':
    app.run(debug=True)
