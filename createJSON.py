import json

def createJSON(jsonType='chain') : 
    try:
        with open('jsonFormats/'+jsonType+'.json') as file :
            jSON = json.load(file)
    except:
        print('check json format')    
    return jSON

if __name__ == "__main__" :
    d = createJSON('token')
    print(d)