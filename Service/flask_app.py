from flask import Flask, request, jsonify
from load_model import *
import base64

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def inference():
    image_data = request.form.get("image_data")
    image = preprocessing_byte(image_data)
    result = predict_function(image)
    result = query_openai(result)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True,port=5003)