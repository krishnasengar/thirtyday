from flask import Flask, jsonify, request ,Response
import json
import datetime 

app = Flask(__name__)

# Route to display the stored JSON data
@app.route('/yoga', methods=['GET'])
def get_data_yoga():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/data', methods=['GET'])
def get_data():
    with open('jss.json', 'r') as file:
        data = json.load(file)
    return Response(json.dumps(data), mimetype='application/json')

# Route to store a value with the key as the current date
def load_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data

def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file)

def update_values(today, value):
    data = load_data()

    if data["d"] == today:
        data["0"] = value
    else:
        for i in range(30, 0, -1):
            data[str(i)] = data[str(i-1)]
        data["1"] = data["0"]
        data["0"] = value
        data["d"]=today

    save_data(data)

@app.route('/update', methods=['POST'])
def update_data():
    today = datetime.datetime.now().day
    value = request.json["value"]
    update_values(today, value)
    return "Data updated successfully!"


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
