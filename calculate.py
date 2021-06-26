import getPrice as gp

def calculate(coin, no): # return value of total coins in usd and inr as dictionary
    coin_price = gp.getPrice(coin)
    usd_val = coin_price['usd'] * no
    inr_val = coin_price['inr'] * no
    return {'usd' : usd_val, 'inr' : inr_val}

def calculateVal(coin_price, no):
    usd_val = coin_price['usd'] * no
    inr_val = coin_price['inr'] * no
    return {'usd' : usd_val, 'inr' : inr_val}