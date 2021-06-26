from terra_sdk.client.lcd import LCDClient
import createJSON as cj
import json
import getPrice as price
import calculate

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

def coinName(coin): #you might have to replace this with dictionary
    switch = {
        'uusd' : 'ust',
        'uluna' : 'luna'
    }
    return switch.get(coin)

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

    for coinDenom in coinList:
        coin = coinName(coinDenom)

        if coinDenom != 'uluna':
            token = cj.createTokenJSON()
            lunaJson['tokens'].append(token)
                     
            lunaJson['tokens'][i]['token'] = coin
            coinBal = getCoinBal(walletBank, coinDenom)
            lunaJson['tokens'][i]['noOfCoins'] = coinBal
            coinPrice = price.getPrice(coin)
            value = calculate.calculateVal(coinPrice, coinBal)
            lunaJson['tokens'][i]['usd_value'] = coinPrice['usd']
            lunaJson['tokens'][i]['total_usd_value'] = value['usd']
            lunaJson['tokens'][i]['total_inr_value'] = value['inr']

            i += 1
            continue

        lunaJson['base']['base'] = coin
        coinBal = getCoinBal(walletBank, coinDenom)
        lunaJson['base']['noOfCoins'] = coinBal
        coinPrice = price.getPrice(coin)
        value = calculate.calculateVal(coinPrice, coinBal)
        lunaJson['base']['usd_value'] = coinPrice['usd']
        lunaJson['base']['total_usd_value'] = value['usd']
        lunaJson['base']['total_inr_value'] = value['inr']
      
    return lunaJson

if __name__ == "__main__" :
    out = getLunaWallet(walletJson)
    print(json.dumps(out))
    with open('jsonFormats/test.json','w') as file :
        file.write(json.dumps(out))
