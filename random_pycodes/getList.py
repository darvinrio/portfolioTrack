from pycoingecko import CoinGeckoAPI
import csv

cg = CoinGeckoAPI()

coin_list = cg.get_coins_list()

keys = coin_list[0].keys()

a_file = open("coinList.csv", "w")
dict_writer = csv.DictWriter(a_file, keys)
dict_writer.writeheader()
dict_writer.writerows(coin_list)
a_file.close()