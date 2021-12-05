
# create a class that mimics the database table: portfolio

class Portfolio():
    def __init__(self, quantity, ticker, purchase_price, account_number: int = -1):
        self.quantity = quantity
        self.ticker = ticker
        self.purchase_price = purchase_price
        self.account_number = account_number
