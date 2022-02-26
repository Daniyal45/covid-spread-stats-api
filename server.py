from flask import Flask
from predict import predict
app = Flask(__name__)

@app.route('/')
def hello_world():
    result = predict()
    return (result)

if __name__ == '__main__':
    app.run()
