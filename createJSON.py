import json

def createBaseJSON():
    with open("jsonFormats/main.json") as file :
        formatDict = json.load(file)

    return formatDict
    # # return base format if no tokens or defi found
    # if(nTokens == 0 and nDefi == 0):
    #     return formatDict

    # # Load token format
    # with open('jsonFormats/token.json') as file :
    #     token = json.load(file)

    # # if non-zero Tokens, make token format, Return format if there is no DeFi
    # if(nTokens != 0):
    #     formatDict['wallet']['tokens'] = []
    #     for i in range(nTokens) :
    #         formatDict['wallet']['tokens'].append(token)
    #     if(nDefi == 0):
    #         return formatDict
    
    # # Load DeFi format
    # with open('jsonFormats/defi.json') as file :
    #     defi = json.load(file)

    # formatDict['defi'] = []
    # for j in range(nDefi) :
    #     formatDict['defi'].append(defi)

    # return formatDict
    
def createTokenJSON() : 
    with open('jsonFormats/token.json') as file :
        token = json.load(file)
    
    return token

def createDefiJSON() : 
    with open('jsonFormats/defi.json') as file :
        defi = json.load(file)
    
    return defi

#if __name__ == "__main__" :
    #d = createJSON(nDefi=3, nTokens=1)
    #print(d)