from flask import Flask
from flask import render_template, request, redirect, abort, jsonify, make_response

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hat.html', title='Регистрация')


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
