from flask import Flask
from src.modular_ml.logger import logging

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    logging.info("TESTING LOGGING FILE")

    return "TESTING TESTING TESTING"


if __name__ == "__main__":
    app.run(debug=True)