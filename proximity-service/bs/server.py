from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "Business Service"


@app.route('/<int:business_id>', methods=['GET'])
def get_business(business_id):
    return jsonify({"business": {"id": business_id}})


if __name__ == '__main__':
    app.run(debug=True)
