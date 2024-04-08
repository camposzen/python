import json
import time

from flask import Flask, request, Response
from flask import abort
from http_constants.headers import HttpHeaders
from http_constants.status import HttpStatus

from transformers import AutoModelForSequenceClassification, AutoTokenizer
from werkzeug.exceptions import HTTPException
from functools import wraps


class Tracker:

    def __init__(self):
        self.counter = 0
        self.start_time = time.time()

    def track(self):
        self.counter += 1
        app.logger.debug(f'Total requests: {self.counter}, Last scrap time: {self.start_time}')

    def reset(self):
        self.counter = 0
        self.start_time = time.time()
        app.logger.debug(f'Tracker reset')
        app.logger.debug(f'Total requests: {self.counter}, Last scrap time: {self.start_time}')


class Moderator:

    def __init__(self):
        # Load the model and tokenizer
        self.model = AutoModelForSequenceClassification.from_pretrained('KoalaAI/Text-Moderation')
        self.tokenizer = AutoTokenizer.from_pretrained('KoalaAI/Text-Moderation')

    def check(self, content: str) -> {str, str}:
        # Run the model on your input
        inputs = self.tokenizer(content, return_tensors='pt')
        outputs = self.model(**inputs)

        # Apply softmax to get probabilities (scores)
        logits = outputs.logits
        probabilities = logits.softmax(dim=-1).squeeze()

        # Retrieve the labels
        id2label = self.model.config.id2label
        labels = [id2label[idx] for idx in range(len(probabilities))]

        # Combine labels and probabilities, then sort
        label_prob_pairs = list(zip(labels, probabilities))
        label_prob_pairs.sort(key=lambda item: item[1], reverse=True)

        # Collect sorted results
        result = {}
        for label, probability in label_prob_pairs:
            result[label] = f'{probability:.4f}'

        return result


app = Flask(__name__)
BASIC_APP_AUTH_KEY = 'AUTHORIZATION4USER'  # TODO: handle multiple

tracker = Tracker()
moderator = Moderator()


def check_authorization(endpoint):
    @wraps(endpoint)
    def decorated_function(*args, **kwargs):
        # verify
        if request.headers.get(HttpHeaders.AUTHORIZATION, None) != BASIC_APP_AUTH_KEY:
            return abort(403)
        # proceed
        app.logger.debug(f'Received request: {request}')  # TODO: probably not needed
        return endpoint(*args, **kwargs)
    return decorated_function


@app.route('/metrics', methods=['GET'])
@check_authorization
def metrics():
    """
        Returns the amount of requests logged and the elapsed time since the last metrics check.
    """
    result = json.dumps({
        'requests': tracker.counter,
        'elapsed_seconds': time.time() - tracker.start_time
    })
    tracker.reset()  # TODO: clarify
    return Response(result, status=HttpStatus.OK, mimetype=HttpHeaders.CONTENT_TYPE_VALUES.json)


@app.route('/moderation', methods=['POST'])
@check_authorization
def moderation():
    """
        Extracts the content parameter from the requests and submits it to validation with the moderator.
    """
    content = request.json['content']
    tracker.track()
    result = json.dumps(moderator.check(content))
    return Response(result, status=HttpStatus.OK, mimetype=HttpHeaders.CONTENT_TYPE_VALUES.json)


@app.errorhandler(Exception)
def handle_error(e):
    app.logger.error(f'Error happened: {e}')
    if isinstance(e, HTTPException):
        result = json.dumps({
                'Error': e.description
            })
        return Response(result, status=e.code, mimetype=HttpHeaders.CONTENT_TYPE_VALUES.json)
    else:
        result = json.dumps({
                'Error': 'Internal server problem.'
            })
        return Response(result, status=HttpStatus.INTERNAL_SERVER_ERROR, mimetype=HttpHeaders.CONTENT_TYPE_VALUES.json)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
