import typing as t
import json
import flask
from flask import Blueprint
import dao
import Investor

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

# 1. Investor a. GET
@app.route('/investor/get-all')
def get_all_investors():
    investors: t.List[Investor] = dao.get_all_investor()
    return json.dumps(investors, default=lambda x: x.__dict__)


@app.route('/investor/<id>')
def get_investor(id):
    investor = dao.get_investor_by_id(id)
    if investor is None:
        return 'Investor does not exist'
    return json.dumps(investor, default=lambda x: x.__dict__)

# JSON: the investor object needs to be encoded into a JSON formatted object that the client can understand


@app.route('/investors/<name>')
def get_investors_by_name(name):
    investors = dao.get_investors_by_name(name)
    if len(investors) == 0:
        return ()
    else:
        return json.dumps(investors, default=lambda x: x.__dict__)

# app.register_blueprint(investor_bp)
# app.register_blueprint(account_bp)
# app.register_blueprint(portfolio_bp)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
