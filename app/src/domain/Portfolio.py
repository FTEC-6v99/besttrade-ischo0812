
# create a class that mimics the database table: portfolio

class Portfolio():
    def __init__(self, quantity: int, ticker: str, purchase_price: float, account_number: int):
        self.quantity = quantity
        self.ticker = ticker
        self.purchase_price = purchase_price
        self.account_number = account_number

    def __str__(self):
        return f'quantity: {self.quantity} | ticker: {self.ticker} | purchase_price: {self.purchase_price} | account number: {self.account_number}'
