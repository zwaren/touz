import logging

from flask import Flask, jsonify, request

from app.comparing_tools import Text
from app.core import compare

app = Flask(__name__)
FISH_TEXT = "Значимость этих проблем настолько очевидна, что сложившаяся структура организации играет важную роль в формировании систем массового участия. Значимость этих проблем настолько очевидна, что рамки и место обучения кадров представляет собой интересный эксперимент проверки позиций, занимаемых участниками в отношении поставленных задач. Не следует, однако забывать, что укрепление и развитие структуры позволяет выполнять важные задания по разработке системы обучения кадров, соответствует насущным потребностям. Разнообразный и богатый опыт постоянное информационно-пропагандистское обеспечение нашей деятельности влечет за собой процесс внедрения и модернизации соответствующий условий активизации. Не следует, однако забывать, что дальнейшее развитие различных форм деятельности представляет собой интересный эксперимент проверки новых предложений. Повседневная практика показывает, что постоянный количественный рост и сфера нашей активности требуют от нас анализа новых предложений."

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


@app.route('/', methods=['POST'])
def texts_compare():
    json_request = request.get_json()
    response = compare(json_request[0], json_request[1])
    return jsonify(response)


@app.route('/text', methods=['GET', 'POST'])
def testing():
    text = Text(FISH_TEXT)
    if request.is_json:
        text = Text(request.get_json())
    return jsonify(text)


if __name__ == '__main__':
    app.run()
