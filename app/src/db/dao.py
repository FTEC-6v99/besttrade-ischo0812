# Database Access Object: file to interface with the database
# CRUD operations:
# C: Create
# R: Read
# U: Update
# D: Delete

import typing as t
from config import dbparams
from mysql.connector import connect, cursor
from mysql.connector.connection import MySQLConnection

from app.src.domain.Investor import Investor
from app.src.domain.Account import Account
from app.src.domain.Portfolio import Portfolio
from app.src.domain.Portfolio import Portfolio1


def get_cnx() -> MySQLConnection:
    return connect(**dbparams)


'''
      Investor DAO functions
'''


def get_all_investors() -> t.List[Investor]:
    '''
        Get list of all investors [R]
    '''
    investors: list[Investor] = []
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True)  # always pass dictionary = True
    sql: str = 'select * from investor'
    cursor.execute(sql)
    results: list[dict] = cursor.fetchall()
    for row in results:
        investors.append(Investor(row['name'], row['status'], row['id']))
    db_cnx.close()
    return investors


def get_investor_by_id(id: int) -> t.Optional[Investor]:
    '''
        Returns an investor object given an investor ID [R]
    '''
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True)  # always pass dictionary = True
    sql: str = 'select * from investor where id = %s'
    cursor.execute(sql, (id,))
    result = cursor.fetchall()
    if len(result) == 0:
        return None
    else:
        row = result[0]
        investor = Investor(row['name'], row['status'], row['id'])
        return investor
    db_cnx.close()


def get_investors_by_name(name: str) -> t.List[Investor]:
    '''
        Return a list of investors for a given name [R]
    '''
    investors: list[Investor] = []
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True)  # always pass dictionary = True
    sql: str = 'select * from investor where name = %s'
    cursor.execute(sql, (name,))
    if cursor.rowcount == 0:
        investors = []
    else:
        rows = cursor.fetchall()
        for row in rows:
            investors.append(Investor(row['name'], row['status'], row['id']))
    db_cnx.close()
    return investors


def create_investor(investor: Investor) -> None:
    '''
        Create a new investor in the db given an investor object [C]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'insert into investor (name, status) values (%s, %s)'
    cursor.execute(sql, (investor.name, investor.status))
    db_cnx.commit()
    db_cnx.close()


def delete_investor(id: int):
    '''
        Delete an investor given an id [D]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'delete from investor where id = %s'
    cursor.execute(sql, (id,))
    db_cnx.commit()  # inserts, updates, and deletes
    db_cnx.close()


def update_investor_name(id: int, name: str) -> None:
    '''
        Updates the investor name [U]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'update investor set name = %s where id = %s'
    cursor.execute(sql, (name, id))
    db_cnx.commit()
    db_cnx.close()


def update_investor_status(id: int, status: str) -> None:
    '''
        Update the investor status [U]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'update investor set status = %s where id = %s'
    cursor.execute(sql, (status, id))
    db_cnx.commit()
    db_cnx.close()


'''
    Account DAO functions
'''


def get_all_accounts() -> t.List[Account]:
    '''
        Get list of all Accounts [R]
    '''
    accounts: list[Account] = []
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True)  # always pass dictionary = True
    sql: str = 'select * from account'
    cursor.execute(sql)
    results: list[dict] = cursor.fetchall()
    for row in results:
        accounts.append(
            Account(row['account_number'], row['investor_id'], row['balance']))
    db_cnx.close()
    return accounts

# ID from Investor table and merge it with Investor_ID in Account table


def get_account_by_id(id: int) -> Account:
    '''
        Returns an account given an ID [R]
    '''
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True)  # always pass dictionary = True
    sql: str = 'select * from account left join investor on account.investor_id=investor.id where investor.id= %s'
    cursor.execute(sql, (id,))
    if cursor.rowcount == 0:
        return None
    else:
        row = cursor.fetchone()
        account = Account(row['account_number'],
                          row['investor_id'], row['balance'])
        return account
    db_cnx.close()


def get_accounts_by_investor_id(investor_id: int) -> t.List[Account]:
    accounts: list[Account] = []
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True)  # always pass dictionary = True
    sql: str = 'select * from account where account.investor_id = %s'
    cursor.execute(sql, (investor_id,))
    results: list[dict] = cursor.fetchall()
    for row in results:
        accounts.append(
            Account(row['account_number'], row['investor_id'], row['balance']))
    db_cnx.close()
    return accounts


def delete_account(account_number: int) -> None:

    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'delete from account where account_number = %s'
    cursor.execute(sql, (account_number,))
    db_cnx.commit()  # inserts, updates, and deletes
    db_cnx.close()


def update_acct_balance(account_number: int, balance: float) -> None:

    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'update account set balance = %s where account_number = %s'
    cursor.execute(sql, (balance, account_number))
    db_cnx.commit()
    db_cnx.close()


def create_account(account: Account) -> None:

    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'insert into account (investor_id, balance) values (%s, %s)'
    cursor.execute(sql, (account.investor_id, account.balance))
    db_cnx.commit()
    db_cnx.close()


'''
    Portfolio DAO functions
'''


def get_all_portfolios() -> t.List[Portfolio]:
    cnx: MySQLConnection = get_cnx()
    cur = cnx.cursor(dictionary=True)
    sql: str = 'select * from portfolio'
    cur.execute(sql)
    rows = cur.fetchall()
    if len(rows) == 0:
        return []
    portfolios = []
    for row in rows:
        portfolios.append(
            Portfolio(row['portfolio_id'], row['account_number'], row['ticker'],
                      row['quantity'], row['purchase_price'])
        )
    cnx.close()
    return portfolios


def get_portfolio_by_acct_no(account_number: int) -> t.List[Portfolio]:
    db_cnx: MySQLConnection = get_cnx()
    cur = db_cnx.cursor(dictionary=True)
    sql = 'select portfolio_id, account_number, ticker, quantity, purchase_price from portfolio where account_number=%s'
    cur.execute(sql, (account_number,))
    rows = cur.fetchall()
    if len(rows) == 0:
        return []
    portfolios = []
    for row in rows:
        portfolios.append(
            Portfolio(row['portfolio_id'], row['account_number'], row['ticker'],
                      row['quantity'], row['purchase_price'])
        )
    db_cnx.close()
    return portfolios


def get_portfolio_by_investor_id(investor_id: int) -> t.List[Portfolio1]:
    # Read
    db_cnx: MySQLConnection = get_cnx()
    cur = db_cnx.cursor(dictionary=True)
    sql = 'select b.investor_id, a.account_number, a.ticker, a.quantity, a.purchase_price from portfolio a left join account b on a.account_number=b.account_number where b.investor_id=%s'
    cur.execute(sql, (investor_id,))
    rows = cur.fetchall()
    if len(rows) == 0:
        return []
    portfolios: list[Portfolio1] = []
    for row in rows:
        portfolios.append(Portfolio1(row['investor_id'], row['account_number'],
                          row['ticker'], row['quantity'], row['purchase_price']))
    db_cnx.close()
    return portfolios


def delete_portfolio(account_number: int, ticker: str) -> None:
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'delete from portfolio where account_number = %s and ticker = %s'
    cursor.execute(sql, (account_number, ticker))
    db_cnx.commit()  # inserts, updates, and deletes
    db_cnx.close()


def buy_stock(account_number: int, ticker: str, buy_price: float, unit: int) -> None:

    unit = int(unit)
    buy_price = float(buy_price)

    # Check Current Price
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor()
    sql: str = 'select balance from account where account_number=%s'
    cursor.execute(sql, (account_number,))
    row = cursor.fetchone()
    current_balance = float(row[0])
    db_cnx.close()

    # Check if funds in the account are sufficient
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor()
    total_purcahse_price = buy_price*unit
    if total_purcahse_price > current_balance:
        print("Insufficient fund in your account")
        return None

    # update new balance
    sql: str = 'update account set balance = balance - %s where account_number = %s'
    cursor.execute(sql, (total_purcahse_price, account_number))
    db_cnx.commit()
    db_cnx.close()

    # create list of stocks in portfolio
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True)
    sql: str = 'select distinct ticker from portfolio where account_number=%s'
    cursor.execute(sql, (account_number,))
    rows = cursor.fetchall()
    stocks: list = []
    for row in rows:
        for key, value in row.items():
            stocks.append(value)
    db_cnx.close()

    # check if ticker in list
    # update quantity
    # insert values
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor()
    if ticker not in stocks:
        sql: str = 'insert into portfolio (account_number, ticker, quantity, purchase_price) values (%s,%s,%s,%s)'
        cursor.execute(sql, (account_number, ticker, unit, buy_price))
        db_cnx.commit()
    else:
        sql: str = 'update portfolio set quantity=quantity+%s where account_number=%s and ticker=%s'
        cursor.execute(sql, (unit, account_number, ticker))
        db_cnx.commit()

    db_cnx.close()

    # get current quantity
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor()
    sql: str = 'select quantity from portfolio where account_number=%s and ticker=%s'
    cursor.execute(sql, (account_number, ticker))
    row = cursor.fetchone()
    current_quantity = row[0]
    db_cnx.close()

    # average purchase price
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor()
    sql: str = 'update portfolio set purchase_price=((purchase_price*%s)+(%s*%s))/(%s+%s)'
    cursor.execute(sql, (current_quantity, unit,
                   buy_price, current_quantity, unit))
    db_cnx.commit()


def sell_stock(account_number: int, ticker: str, sell_price: float, unit: int) -> None:

    # sale_price*volume to get total dollars
    unit = int(unit)
    # get current quantity
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor()
    sql: str = 'select quantity from portfolio where account_number=%s and ticker=%s'
    cursor.execute(sql, (account_number, ticker))
    row = cursor.fetchone()
    current_quantity = int(row[0])
    db_cnx.close()

    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor()
    if current_quantity < unit:
        print("You do not have sufficient shares to sell")
        return None

    elif current_quantity == unit:
        sql: str = 'delete from portfolio where account_number=%s and ticker=%s'
        cursor.execute(sql, (account_number, ticker))
        db_cnx.commit()

    elif current_quantity > unit:
        sql: str = 'update portfolio set quantity=%s-%s where account_number=%s and ticker=%s'
        cursor.execute(sql, (current_quantity, unit, account_number, ticker))
        db_cnx.commit()
    db_cnx.close()

    # update balance with total sale price
    total_sales_price = sell_price*unit
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor()
    sql: str = 'update account set balance= balance + %s where account_number = %s'
    cursor.execute(sql, (total_sales_price, account_number))
    db_cnx.commit()

    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor()
    sql: str = 'delete from portfolio where quantity=0'
    cursor.execute(sql)
    db_cnx.commit()
    db_cnx.close()
