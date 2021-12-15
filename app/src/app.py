import typing as t
import flask
from app.src.blueprints.investorbp import investor_bp
from app.src.blueprints.accountbp import account_bp
from app.src.blueprints.portfoliobp import portfolio_bp
from app.src.blueprints.homebp import home_bp
from app.src.blueprints.aboutbp import about_bp
from app.src.blueprints.uibp import ui_bp

application = app = flask.Flask(__name__)


app.register_blueprint(investor_bp)
app.register_blueprint(account_bp)
app.register_blueprint(portfolio_bp)
app.register_blueprint(home_bp)
app.register_blueprint(about_bp)
app.register_blueprint(ui_bp)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
