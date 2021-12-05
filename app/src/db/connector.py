from mysql.connector import connect


def main():
    cnx = connect(
        host='ftecv99.cbjsrvmj1rmx.us-west-2.rds.amazonaws.com',
        username='admin',
        password='HiDrBourji',
<<<<<<< HEAD
        database='ftec6v99'
=======
        database='ftec6v99',
>>>>>>> b0fe587729f5e648600eaf26655e93a2deafb727
    )

    cursor = cnx.cursor()
    sql = 'select * from investor'
    cursor.execute(sql)
    investors = cursor.fetchall()
    for investor in investors:
        print(investor)


if __name__ == '__main__':
    main()
