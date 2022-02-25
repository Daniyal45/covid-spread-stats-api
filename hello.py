from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h2> Covid Spread Stats Service </h2>'

if __name__ == '__main__':
    app.run()
