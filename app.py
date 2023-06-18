import json
from flask import Flask, Response

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    with open('jss.json', 'r') as file:
        data = json.load(file)
    return Response(json.dumps(data), mimetype='application/json')

if __name__ == '__main__':
    app.run()



