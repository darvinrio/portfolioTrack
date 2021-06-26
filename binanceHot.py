from binance.client import Client
import private.key as bKey

client = Client(bKey.key,bKey.secret)

details = client.get_account()
balance = details['balances']
print(balance)