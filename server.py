from flask import Flask, request
from csv_generator import generate_csv
import json

app = Flask(__name__)

@app.route('/predict')
def hello_world():
    country = request.args['country']
    result = generate_csv(country)
    return (json.dumps(result))

if __name__ == '__main__':
    app.run()
