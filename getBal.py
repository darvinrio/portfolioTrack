import ban
import pandas as pd

f_df = pd.read_csv('data/coinFunctions.csv') # stores function and the coin related to it 

def getBalance(address, coin): #address, coin
    
    func = f_df[f_df['coin'] == coin]
    f = func.iloc[0,1]
    func_str = f+"('"+address+"')"
    bal = eval(func_str)
    return bal


#print(getBalance(wal,c))