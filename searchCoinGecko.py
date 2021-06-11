import pandas as pd

coinList = pd.read_csv('data/coinList.csv')

def searchToken(coinSym):
    coin = coinList[coinList['symbol'] == coinSym]
    return coin

#print(searchToken('ban'))