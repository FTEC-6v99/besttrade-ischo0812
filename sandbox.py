
import app.src.db.dao as dao


def main():
    popular_stocks = dao.get_popular_stocks()
    for stock in popular_stocks:
        print(stock)


if __name__ == '__main__':
    main()
