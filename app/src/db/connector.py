from mysql.connector import connect


def main():
    cnx = connect(
        host='ftecv99.cbjsrvmj1rmx.us-west-2.rds.amazonaws.com',
        username='admin',
        password='HiDrBourji',
        database='ftec6v99',
    )

    cursor = cnx.cursor()
    sql = 'select * from investor'
    cursor.execute(sql)
    investors = cursor.fetchall()
    for investor in investors:
        print(investor)


if __name__ == '__main__':
    main()
