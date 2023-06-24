from flask import Flask, jsonify, request
import json
from datetime import date

app = Flask(__name__)

# Route to display the stored JSON data
@app.route('/data', methods=['GET'])
def get_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

# Route to store a value with the key as the current date
@app.route('/store', methods=['POST'])
def store_data():
    value = request.json.get('value')  # Extract value from JSON payload
    today = str(date.today().day)

    with open('data.json', 'r') as file:
        data = json.load(file)

    data[today] = value

    with open('data.json', 'w') as file:
        json.dump(data, file)

    return 'Value stored successfully.'

# Route to retrieve the value of a specific date
@app.route('/value/<number>', methods=['GET'])
def get_value(number):
    if not number.isdigit() or int(number) > 31:
        return '0'  # Return 0 for invalid or out-of-range dates

    with open('data.json', 'r') as file:
        data = json.load(file)

    value = data.get(number)
    if value is not None:
        return str(value)
    else:
        return 'No value found for the specified date.'

if __name__ == '__main__':
    app.run()
