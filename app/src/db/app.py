import typing as t
import flask
import dao

application = app = flask.Flask(__name__)


# @app.route('/')
# def default():
#     return 'Hello world'


# @app.route('/say-hi')
# def say_hi():
#     return 'hi!'


# @app.route('/say-hello')
# def say_hello():
#     return 'hello!'


@app.route('/investor/get-all')
def get_all_investors():
    investors: t.List[Investor] = dao.get_all_investor()
    return investors


@app.route('/investor/<id>')
def get_investor(id):
    investor = dao.get_investor_by_id(id)
    if investor is None:
        return 'Investor does not exist'
    return str(investor)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
