from pycoingecko import CoinGeckoAPI
import searchCoinGecko as scg

cg = CoinGeckoAPI()

def getPrice(coinSym): #return value of each coinSym in usd and inr
    coinID = scg.searchToken(coinSym).iloc[0,0]
    x = cg.get_price(ids=coinID, vs_currencies=['usd','inr']) #returns dict
    return x[coinID] #extract and return price list 

