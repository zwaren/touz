from flask import Flask, jsonify, request
from app.core import compare
app = Flask(__name__)


@app.route('/')
def index():
    json_data = {'Hello': 'World!'}
    return jsonify(json_data)


@app.route('/texts/', methods=['POST'])
def texts_compare():
    json_request = request.get_json()
    response = compare(json_request[0], json_request[1])
    return jsonify(response)


if __name__ == '__main__':
    app.run()
