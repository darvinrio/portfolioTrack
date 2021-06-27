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
lunaPrice = price.getPrice('luna')

def getCoinValBase(denom):
    exchangeRate = (terra.oracle.exchange_rates()).get(denom)
    exchangeRateDec = ((exchangeRate.to_data())['amount'])

    baseVal = 1/float(exchangeRateDec)
    return baseVal


def getCoinBal(Coin, coinDenom, coinType='token'): #coinType = base for baseToken

    coin = coinName(coinDenom)
    token = cj.createJSON(coinType)

    coinBalInt = Coin.to_data()['amount']
    coinBal = float(coinBalInt)/(10**6)
    coinPrice = price.getPrice(coin)
    value = calculate.calculateVal(coinPrice, coinBal)

    token[coinType] = coin
    token['noOfCoins'] = coinBal
    token['usd_value'] = coinPrice['usd']
    token['total_usd_value'] = value['usd']
    token['total_inr_value'] = value['inr']

    if(coinType == 'base'):
        return token
    else:
        baseVal = getCoinValBase(coinDenom)
        token['base_value'] = baseVal
        token['total_base_value'] = coinBal * baseVal

    return token


def coinName(coin): #you might have to replace this with dictionary
    switch = {
        'uusd' : 'ust',
        'uluna' : 'luna'
    }
    return switch.get(coin)


def getLunaWallet(wallet):
    walletBank = terra.bank.balance(wallet['address'])
    coinList = walletBank.denoms()
    lunaJson =  cj.createJSON()

    lunaJson['walletName'] = wallet['name']
    lunaJson['network'] = 'luna'
    lunaJson['wallet_address'] = wallet['address']
    noOfCoins = len(coinList)
        
    if(  noOfCoins > 1 ) :
        lunaJson['tokens'] = []
    
    i = 0

    for coinDenom in coinList:
        #coin = coinName(coinDenom)
        coin = walletBank.get(coinDenom)

        if coinDenom != 'uluna':
            token = getCoinBal(coin, coinDenom)
            lunaJson['tokens'].append(token)
            
            continue

        base = getCoinBal(coin, coinDenom, 'base')
        lunaJson['base']= base    
        
      
    return lunaJson


def lunaStaking(wallet):
    lunaStake = terra.staking.delegations(delegator = wallet['address'])
    lunaRew = terra.distribution.rewards(wallet['address'])

    stake = cj.createJSON('stake')
    stake['token'] = 'luna'

    delegations = []

    for delegation in lunaStake:
        stakeTemp = cj.createJSON('delegation')

        val = terra.staking.validator(delegation.validator_address)
        stakeTemp['validator'] = (val.description.moniker)
        stakeTemp['validatorAddress'] = (delegation.validator_address)

        noOfStakedCoins = delegation.balance.to_data()['amount']
        coinBal = stakeTemp["noOfStakedCoins"] = float(noOfStakedCoins)/(10**6)
        stakeTemp['usd_value'] = lunaPrice
        value = calculate.calculateVal(lunaPrice, coinBal)
        stakeTemp['total_usd_value'] = value['usd']
        stakeTemp['total_inr_value'] = value['inr']

        rewardCoins = lunaRew.rewards[delegation.validator_address]
        coinList = rewardCoins.to_data()
        print(coinList)

        
        delegations.append(stakeTemp)

    stake['delegations'] = delegations
    return stake


def getStakingReward(wallet):
    lunaRew = terra.distribution.rewards(wallet['address'])
    coins = lunaRew.rewards
    print(coins)
    #coinList = coins.denoms()
    #return coinList


if __name__ == "__main__" :
    var = getLunaWallet(walletJson)
    # for dele in var:
    #     var2 = var[dele]
    #     print(var2)
    #     print(type(var2))
    print(var)
    # print(type(var))
