# Trader Object
class Trader(object):
    """docstring for trader"""

    def __init__(self, first_name, last_name, risk_version, portfolio=[]):
        super(Trader, self).__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.risk_version = risk_version
        self.portfolio = portfolio
        self.full_name = self.first_name + ' ' + self.last_name

    # check if traders is already registered
    def exists(self):
        return check_trader_exists(self.full_name, traders_list)

    def get_portfolio(self):
        display_portfolio = ''
        for each in self.portfolio:
            display_portfolio = display_portfolio + each + ','
        return display_portfolio


# Portfolio Object
class Portfolio(object):
    """docstring for portfolio"""

    def __init__(self, belongsto, stocks):
        super(Portfolio, self).__init__()
        self.belongsto = belongsto
        self.stocks = stocks

    def get_value(self):
        return value

    def buy_stock(self):
        # buy a stock and to portfolio
        return

    def sell_stock(self):
        # sell a stock and remove from portfolio
        return

    def remove_stock(self):
        pass


# Stock Object
class Stock(object):
    def __init__(self, code, asset_type, price, year_change, ):
        super(Stock, self).__init__()
        self.price = price
        self.code = code
        self.asset_type = asset_type


# Methods
def buy_sell_hold(stock):
    return recommendation


def check_trader_exists(tradername, traders_list):
    for each in traders_list:
        if each.full_name == tradername:
            return True
        else:
            return False


# print out details for a trader
def get_trader_details(fullname):
    for each in traders_list:
        if each.full_name == fullname:
            print(each.full_name)
            print(each.risk_version)
            print(each.get_portfolio())


traders_list = []  # list of traders ( from SQL or in memory)
portfolios_list = []  # list of portfolios ( from SQL or in memory)

# create a new trader(s), hardcoded or inputed by user
trader1 = Trader('Asen', 'Kolev', 100, ['IBM', 'GM', 'XYX'])
trader2 = Trader('Peter', 'Ivanov', 100, ['IBM', 'GM', 'XYX'])

# Add traders to list, if they don't already exist
if not trader1.exists(): traders_list.append(trader1)
if not trader2.exists(): traders_list.append(trader2)

print(trader1.full_name)
print('Portfolio:' + trader1.get_portfolio())
print('Trader Risk Aversion: ' + str(trader1.risk_version))

print('------------------------')

print(trader2.full_name)
print('Portfolio:' + trader2.get_portfolio())
print('Trader Risk Aversion: ' + str(trader2.risk_version))

trader3 = Trader('Asen2', 'Kolev', 90, ['IBM', 'GM', 'XYX'])

if not trader3.exists():
    traders_list.append(trader3)

print('------------------------')
print('Current Registered Traders:')

# get_trader_details('Asen Kolev')
for each in traders_list:
    print(each.full_name + " " + str(each.risk_version))