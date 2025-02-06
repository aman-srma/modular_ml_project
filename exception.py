from flask import Flask
from src.modular_ml.logger import logging
from src.modular_ml.exception import CustomException
import os, sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    try:
        raise Exception("TESTING EXCEPTION FILE")
    except Exception as e:
        ML = CustomException(e, sys)
        logging.info(ML.error_message)

        logging.info("HBDFBHSDFHS")

        return "TESTING TESTING TESTING EXCEPTION"


if __name__ == "__main__":
    app.run(debug=True)