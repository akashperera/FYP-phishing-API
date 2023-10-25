
from flask import Flask, request, jsonify
from API import get_prediction
app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def index():
    return "Hello World"


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    url = data['url']
    model_path = r"/home/ap101/phish/gbcmodel.pkl"
    prediction = get_prediction(url,model_path)
    return jsonify(prediction)


if __name__ == '__main__':
    app.run(port=5000, debug=True)