from flask import Blueprint, render_template

home_bp = bp = Blueprint('home', __name__, url_prefix='/home')


@bp.route('/')
def default():
    return render_template('home.html')
