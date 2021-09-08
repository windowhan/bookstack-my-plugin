import json 

def readFile(path):
    fp = open(path, "r")
    data = fp.read()
    fp.close()
    return data

def readConfig(path):
    data = readFile(path)
    return json.loads(data)
