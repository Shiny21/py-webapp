import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "hello world!"

@app.route('/name')
def hello():
    return 'brutus'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
