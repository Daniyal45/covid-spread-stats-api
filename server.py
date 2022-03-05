from flask import Flask, request
from flask_cors import CORS, cross_origin
from csv_generator import generate_csv
import json

app = Flask(__name__)
CORS(app)

@app.route('/predict')
def hello_world():
    country = request.args['country']
    result = generate_csv(country)
    return (json.dumps(result))

if __name__ == '__main__':
    app.run()
