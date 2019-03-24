from flask import Flask, jsonify, request
from app.core import compare
import logging
app = Flask(__name__)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

@app.route('/', methods=['POST'])
def texts_compare():
    json_request = request.get_json()
    response = compare(json_request[0], json_request[1])
    return jsonify(response)


if __name__ == '__main__':
    app.run()
