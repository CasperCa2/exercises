class Money:

    def __init__(self, money_currency, money_type):

        self.money_currency = money_currency
        self.money_type = money_type

    def currency(self):
        return self.money_type

    def amount(self):
        return self.money_currency

    def __add__(self, other):
        if self.money_type == other.money_type:
            self.money_currency = self.money_currency + other.money_currency
        return self.money_currency

    def __sub__(self, other):
        if self.money_type == other.money_type:
            self.money_currency = self.money_currency - other.money_currency

    def __mul__(self, int):
        self.money_currency = self.money_currency * int
