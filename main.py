import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "boas-vindas!"

@app.route('/como está')
def hello():
    return 'Eu estou ótimo'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
