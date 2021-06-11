import pandas as pd 
import multiprocessing as mp
import ban
import calculate
import getPrice
import asyncio
#----------------------------------------------------------

wallets = pd.read_csv('private/wallets.csv')

wallets['coins'] = 0
wallets['usd_value'] = 0
wallets['inr_value'] = 0

def getIt(row):
    row[3] = ban.getBalance(row[2])
    row[4] = getPrice.getPrice(row[1])
    row[5] = row[4]*row[5]
    #print(row[0])

#cpu = mp.cpu_count()

#with mp.Pool(cpu) as pool :
#    pool.map(getIt, wallets.itertuples(name=None))

print(wallets.head())
test = ['kaliumMain','ban','ban_3mu93fpkbmfuh99jqoq148ge4mgfq5xraeu94mkzno9atc5cy7oqrpjeypxr']

print(type(test))
getIt(test)