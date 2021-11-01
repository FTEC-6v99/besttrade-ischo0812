class Portfolio():
    # create a class that mimics the database table: portfolio
    def __init__(self, account_number, ticker, quantity, purchase_price):
        self.account_number = account_number
        self.ticker = ticker
        self.quantity = quantity
        self.purchase_price = purchase_price
    pass
