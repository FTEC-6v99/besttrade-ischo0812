import dao
import Investor


def main():
    investors = dao.get_all_investor()
    for investor in investors:
        print(investor)


if __name__ == '__main__':
    main()
