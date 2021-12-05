import flask

application = app = flask.Flask(__name__)


@app.route('/')
def default():
    return 'Hello world'


if __name__ == '__main__':
    app.run(port=8080)
