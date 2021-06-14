import pandas as pd 
import multiprocessing as mp
import ban
import calculate
import getPrice
import asyncio
#----------------------------------------------------------

wallets = pd.read_csv('private/wallets.csv')

def getIt(row):
    
    # get row label
    l = row[0] 

    # setup output dict
    outDict = {
        'wallet_name' : row[1], # store wallet name
        'coin' : row[2],        # store coin name
        'address': row[3],      # store wallet address
        'coin_no' : 0,
        'usd_value' : 0,
        'inr_value' : 0 
    }
     
    # get wallet balance
    outDict['coin_no'] = ban.getBalance(outDict['address'])

    # calculate value of coins
    value = calculate.calculate(wallets.iloc[l,1],outDict['coin_no'])

    #store 
    outDict['usd_value'] = value['usd']
    outDict['inr_value'] = value['inr']
    
    return outDict

cpu = mp.cpu_count()

#with mp.Pool(cpu) as pool :
#    x = pool.map(getIt, wallets.itertuples(name=None))

def printOut():

    # call multiprocess for each row and get List of Dicts
    with mp.Pool(cpu) as pool :
        outDicts = pool.map(getIt, wallets.itertuples(name=None))

    #convert List of Dicts to DF
    d = pd.DataFrame(outDicts)
    
    print(d)
    

printOut()

