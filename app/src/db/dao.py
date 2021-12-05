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
from app.src.domain.Portfolio import Portfolio
from app.src.domain.Account import Account


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


def get_accounts_by_investor_id(investor_id: int) -> t.List[Account]:

    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True)  # always pass dictionary = True
    sql: str = 'select * from account left join investor on account.investor_id=investor.id where account.investor_id = %s'
    cursor.execute(sql, (investor_id,))
    if cursor.rowcount == 0:
        return None
    else:
        row = cursor.fetchone()
        account = Account(row['account_number'],
                          row['investor_id'], row['balance'])
        return account


def delete_account(investor_id: int) -> None:

    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'delete from account where investor_id = %s'
    cursor.execute(sql, (investor_id,))
    db_cnx.commit()  # inserts, updates, and deletes
    db_cnx.close()


def update_acct_balance(investor_id: int, account_balance: float) -> None:

    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'update account set account_balance = %s where investor_id = %s'
    cursor.execute(sql, (investor_id, account_balance))
    db_cnx.commit()
    db_cnx.close()


def create_account(account: Account) -> None:

    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'insert into account (account_number, investor_id, balance) values (%s, %s, %s)'
    cursor.execute(sql, (account.account_number,
                   account.investor_id, account.balance))
    db_cnx.commit()
    db_cnx.close()


'''
    Portfolio DAO functions
'''


def get_all_portfolios() -> t.List[Portfolio]:
    '''
        Get list of all portfolios [R]
    '''
    portfolios: list[Portfolio] = []
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True)  # always pass dictionary = True
    sql: str = 'select * from portfolio'
    cursor.execute(sql)
    results: list[dict] = cursor.fetchall()
    for row in results:
        portfolios.append(Portfolio(row['portfolio_id'], row['account_number'],
                          row['ticker'], row['quantity'], row['purchase_price']))
    db_cnx.close()
    return portfolios


def get_porfolios_by_acct_id(account_number: int) -> t.List[Portfolio]:

    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True)  # always pass dictionary = True
    sql: str = 'select * from portfolio where account_number = %s'
    cursor.execute(sql, (account_number))
    if cursor.rowcount == 0:
        return None
    else:
        row = cursor.fetchone()
        portfolio = Portfolio(row['portfolio_id'], row['account_number'],
                              row['ticker'], row['quantity'], row['purchase_price'])
        return portfolio


def get_portfolios_by_investor_id(investor_id: int) -> t.List[Portfolio]:
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True)  # always pass dictionary = True
    sql: str = 'select * from portfolio left join account on account.account_number = portfolio.account_number where investor_id = %s'
    cursor.execute(sql, (investor_id))
    if cursor.rowcount == 0:
        return None
    else:
        row = cursor.fetchone()
        portfolio = Portfolio(row['portfolio_id'], row['account_number'], row['ticker'],
                              row['quantity'], row['purchase_price'], row['investor_id'])
        return portfolio


def delete_portfolio(id: int) -> None:
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'delete from portfolio where account_number = (select account_number from investor left join account on id=investor_id where id= %s)'
    cursor.execute(sql, (id,))
    db_cnx.commit()  # inserts, updates, and deletes
    db_cnx.close()


def buy_stock(ticker: str, price: float, quantity: int) -> None:
    # code goes here creating a new row in portfolio
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'insert into porfolio(ticker,price, quantity) values(%s, %s,%s)'
    cursor.execute(sql, (ticker, price, quantity))
    db_cnx.commit()  # inserts, updates, and deletes
    db_cnx.close()


def sell_stock(ticket: str, quantity: int, sale_price: float) -> None:

    # def update_stockqty(ticker: str, quantity: int) -> None:
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'update portfolio set stock_qty=10 where ticker=MSFT'
    cursor.execute(sql, (ticker, quantity))
    db_cnx.commit()
    db_cnx.close()
    return update_stockqty


def update_account_balance(investor_id: int, balance: float) -> None:
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'update account set balance=100 where investor_id=1'
    cursor.execute(sql, (investor_id, balance))
    db_cnx.commit()
    db_cnx.close()
    return update_account_balance


def update_stockqty(ticker: str, quantity: int) -> None:
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'update portfolio set stock_qty=7 where ticker=MSFT'
    cursor.execute(sql, (ticker, quantity))
    db_cnx.commit()
    db_cnx.close()
    return update_stockqty


def update_account_balance(investor_id: int, balance: float) -> None:
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'update account set balance=110 where investor_id=1'
    cursor.execute(sql, (investor_id, balance))
    db_cnx.commit()
    db_cnx.close()
    return update_account_balance
