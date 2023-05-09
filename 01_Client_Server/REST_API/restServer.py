# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
import argparse
import os, sys
import uuid
import pathlib
import json
import subprocess
import logging
import jsonschema

from dotenv import load_dotenv
from flask import Flask, request


load_dotenv()
#!flask/bin/python

app = Flask(__name__)

def parse_body(api_request):

    body = '{}'

    if len(api_request.form) == 0:
        return 0, body

    try:
        body = json.loads(str(api_request.form['body']))
        return 0, body

    except json.decoder.JSONDecodeError as err:
        print(err)
    except Exception as err:
        print(err)


@app.route('/status/<status_id>', methods=['GET'])
def get_tasks(status_id):
    """REST API GET entry point """

    print(status_id)
    return status_id



@app.route('/order', methods=['PUT'])
def update_task():
    """REST API PUT entry point """
    error, body = parse_body(request)
    if error:
        return error
    print(body)
    audio = request.files["audio"]
    return f"body:{body}, audio_filename: {audio.filename}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version='%(prog)s 0.7')
    args = parser.parse_args()

    app.run(port=4242, debug=True)

    # from waitress import serve
    # serve(app, host="0.0.0.0", port=4242)


if __name__ == '__main__':
    main()
