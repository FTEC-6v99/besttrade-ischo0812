from flask import Blueprint, render_template
import app.src.db.dao as dao

ui_bp = bp = Blueprint('ui', __name__, url_prefix='/ui')


@bp.route('/', methods=['GET'])
def main():
    return render_template('home.html')


# @bp.route('/about', methods=['GET'])
# def about():
#     return render_template('about.html')

@bp.route('/about')
def about():
    popular_stocks = dao.get_popular_stocks()
    data = {
        'stocks': popular_stocks
    }
    return render_template('about.html', **data)


# @bp.route('/investors', methods=['GET'])
# def investor():
#     return render_template('investors.html')

@bp.route('/investors', methods=['GET'])
def investor():
    all_investors = dao.get_investors()
    data = {
        'investors': all_investors
    }
    return render_template('investors.html', **data)

# @bp.route('/investors', methods=['GET'])
# def investor():
#     investors = dao.get_investors()
#     return render_template('investors.html', investors=investors)
