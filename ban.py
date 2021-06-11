import subprocess as sp
import numpy as np
#--------------------------------------------------

def getBalance(wallet):
    x = sp.run(['npm', '--prefix', 'banano/node_modules/@bananocoin/bananojs/', 'start', 'baccountinfo', wallet], capture_output=True, text=True)
    res = x.stdout
    resArr = res.split()
    #properPrint(resArr)
    ban_str = (resArr[42])
    banoshi_str = (resArr[44])

    ban = ban_str[1:len(ban_str)-2]
    banoshi = banoshi_str[1:len(banoshi_str)-2]
    
    total_ban = float(ban) + float(banoshi) / 100
    return total_ban

def properPrint(arr):
    i=0
    for s in arr :
        print(str(i)+" > "+s)
        i += 1

#getBalance('ban_3mu93fpkbmfuh99jqoq148ge4mgfq5xraeu94mkzno9atc5cy7oqrpjeypxr')