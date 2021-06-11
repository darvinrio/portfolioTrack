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

print(wallets.head())

def getIt(row):
    # get row label
    l = row[0] 

    # get wallet balance
    wallets.iloc[l,3] = ban.getBalance(wallets.iloc[l,2])

    # calculate value of coins
    value = calculate.calculate(wallets.iloc[l,1],wallets.iloc[l,3])

    print(value)

    #store 
    wallets.iloc[l,4] = value[0]
    wallets.iloc[l,5] = value[1]
    print(wallets.head())

cpu = mp.cpu_count()

with mp.Pool(cpu) as pool :
    pool.map(getIt, wallets.itertuples(name=None))

print(wallets.head())
