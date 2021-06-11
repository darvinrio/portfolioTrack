import pandas as pd 
import multiprocessing as mp
import ban
import calculate
import getPrice
import asyncio
#----------------------------------------------------------

wallets = pd.read_csv('private/wallets.csv')

def getIt(row):
    
    # setup output dict
    output = {
        'coin' : 0,
        'usd_value' : 0,
        'inr_value' : 0 
    }
    # get row label
    l = row[0] 
  
    # get wallet balance
    output['coin'] = ban.getBalance(wallets.iloc[l,2])

    # calculate value of coins
    value = calculate.calculate(wallets.iloc[l,1],output['coin'])

    print(value)

    #store 
    output['usd_value'] = value['usd']
    output['inr_value'] = value['inr']
    
    return output

cpu = mp.cpu_count()

with mp.Pool(cpu) as pool :
    pool.map(getIt, wallets.itertuples(name=None))

