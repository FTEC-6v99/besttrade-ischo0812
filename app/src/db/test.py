import typing as t
from mysql.connector import connect, cursor
from mysql.connector.connection import MySQLConnection

from app.src.domain.Investor import Investor
from app.src.domain.Account import Account
from app.src.domain.Portfolio import Portfolio
