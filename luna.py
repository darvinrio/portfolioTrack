from terra_sdk.client.lcd import LCDClient

wallet = 'terra1jse8nzxu5uf9tq5m4rw9v0hhqcfutahay6zj74'

terra = LCDClient(chain_id="columbus-4", url="https://lcd.terra.dev")

#print(terra.auth.account_info(wallet))
#print(terra.bank.balance(wallet))
bal = terra.bank.balance(wallet)

print(bal.to_data()[1])