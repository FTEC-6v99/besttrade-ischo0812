from mysql.connector import connect


def main():
    cnx = connect(
        host='ftecv99.cbjsrvmj1rmx.us-west-2.rds.amazonaws.com',
        username='admin',
        password='HiDrBourji',
        database='ftec6v99'
    )

    cursor = cnx.cursor()
    sql = 'select * from account'
    cursor.execute(sql)
    accounts = cursor.fetchall()
    for account in accounts:
        print(account)


if __name__ == '__main__':
    main()
