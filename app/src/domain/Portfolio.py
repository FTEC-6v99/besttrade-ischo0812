
# create a class that mimics the database table: portfolio

class Portfolio():
    def __init__(self, portfolio_id: int, account_number: int, ticker: str,  quantity: int, purchase_price: float, ):
        self.portfolio_id = portfolio_id
        self.account_number = account_number
        self.ticker = ticker
        self.purchase_price = purchase_price
        self.quantity = quantity

    # def __str__(self):
    #     return f'quantity: {self.quantity} | ticker: {self.ticker} | purchase_price: {self.purchase_price} | account number: {self.account_number}'


class Portfolio1():
    def __init__(self, investor_id: int, account_number: int, ticker: str,  quantity: int, purchase_price: float, ):
        self.investor_id = investor_id
        self.account_number = account_number
        self.ticker = ticker
        self.purchase_price = purchase_price
        self.quantity = quantity

    # def __str__(self):
    #     return f'quantity: {self.quantity} | ticker: {self.ticker} | purchase_price: {self.purchase_price} | account number: {self.account_number}'
