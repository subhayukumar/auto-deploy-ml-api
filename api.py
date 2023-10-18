import os
import sys
from urllib.request import urlretrieve

import joblib
import pandas as pd
from flask import Flask, request, jsonify


app = Flask(__name__)

MODEL_PATH = "model.pkl"
MODEL_URL = os.getenv("MODEL_URL")
MODEL_COLS = [
    "Age",
    "Embarked_C",
    "Embarked_Q",
    "Embarked_S",
    "Embarked_nan",
    "Sex_female",
    "Sex_male",
    "Sex_nan",
]

if MODEL_URL:
    try:
        urlretrieve(MODEL_URL, filename=MODEL_PATH)
        print("Model downloaded")
    except Exception as e:
        print(f"Unable to download model, Error: {e}")
        exit(1)

try:
    MODEL = joblib.load(MODEL_PATH)
    print("Model loaded")
except Exception as e:
    print(f"Unable to load model, Error: {e}")
    exit(1)



@app.route("/predict/columns", methods=["GET"])
def get_schema():
    """
    Endpoint for getting the schema of the model

    Returns:
        response (str or JSON): The schema of the model
    """
    return jsonify({"columns": MODEL_COLS})


@app.route("/predict/example", methods=["GET"])
def get_example():
    """
    Endpoint for getting an example of the model input and output data

    Returns:
        response (str or JSON): The example of the model input and output data
    """
    return jsonify({
        "input": [
            {"Age": 24, "Sex": "male", "Embarked": "S"},
            {"Age": 24, "Sex": "male", "Embarked": "C"},
            {"Age": 24, "Sex": "male", "Embarked": "Q"},
            {"Age": 24, "Sex": "female", "Embarked": "S"},
            {"Age": 24, "Sex": "female", "Embarked": "C"},
            {"Age": 24, "Sex": "female", "Embarked": "Q"},
        ],
        "output": [0, 0, 0, 1, 1, 1]
    })


@app.route("/predict", methods=["POST"])
def predict():
    """
    Endpoint for making predictions based on input data

    Returns:
        response (str or JSON): The prediction result or error message
    """
    if MODEL:
        try:
            json_data = request.json
            query = pd.get_dummies(pd.DataFrame(json_data))
            query = query.reindex(columns=MODEL_COLS, fill_value=0)
            prediction = MODEL.predict(query)
            return jsonify({"prediction": [int(x) for x in prediction]})
        except Exception as e:
            return jsonify({"trace": str(e)})
    else:
        return "No model here to use"


if __name__ == "__main__":
    try:
        port = int(sys.argv[1])
    except:
        port = 8080

    app.run(port=port, debug=True)
