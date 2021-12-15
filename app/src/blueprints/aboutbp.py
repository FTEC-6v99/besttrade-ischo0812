from flask import Blueprint, render_template
import app.src.db.dao as dao

about_bp = bp = Blueprint('about', __name__, url_prefix='/about')


@bp.route('/')
def about():
    popular_stocks = dao.get_popular_stocks()
    data = {
        'stocks': popular_stocks
    }
    return render_template('about.html', **data)
