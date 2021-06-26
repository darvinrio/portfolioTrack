from terra_sdk.client.lcd import LCDClient
import createJSON as cj
import json
import getPrice as price

wallet = 'terra1jse8nzxu5uf9tq5m4rw9v0hhqcfutahay6zj74'

walletJson = {
    "name" : 'terraStation',
    "address" : 'terra1jse8nzxu5uf9tq5m4rw9v0hhqcfutahay6zj74'
} 

terra = LCDClient(chain_id="columbus-4", url="https://lcd.terra.dev")


def getCoinBal(wallet, coin):
    bal = wallet
    coinBal = bal.get(coin).to_data()['amount']
    properCoin = float(coinBal)/(10**6) 
    return properCoin

def getLunaWallet(wallet):
    walletBank = terra.bank.balance(wallet['address'])
    coinList = walletBank.denoms()
    lunaJson =  cj.createBaseJSON()

    lunaJson['walletName'] = wallet['name']
    lunaJson['network'] = 'luna'
    lunaJson['wallet_address'] = wallet['address']
    noOfCoins = len(coinList)
        
    if(  noOfCoins > 1 ) :
        lunaJson['tokens'] = []
    
    i = 0

    for coin in coinList:
        if coin != 'uluna':
            token = cj.createTokenJSON()
            lunaJson['tokens'].append(token)
            
            lunaJson['tokens'][i]['token'] = coin
            lunaJson['tokens'][i]['noOfCoins'] = getCoinBal(walletBank, coin)
        
            i += 1
            continue

        lunaJson['base']['base'] = 'luna'
        lunaJson['base']['noOfCoins'] = getCoinBal(walletBank, coin)
        coinPrice = price.getPrice('luna')
        lunaJson['base']['usd_value'] = coinPrice['usd']
        

    return lunaJson

if __name__ == "__main__" :
    out = getLunaWallet(walletJson)
    print(json.dumps(out))
