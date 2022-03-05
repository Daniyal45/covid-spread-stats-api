from urllib import response
from flask import Flask, request, jsonify
from csv_generator import generate_csv
import json

app = Flask(__name__)

@app.route('/predict')
def hello_world():
    country = request.args['country']
    result = generate_csv(country)
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return (response)

if __name__ == '__main__':
    app.run()
