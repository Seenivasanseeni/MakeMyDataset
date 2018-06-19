import json

def readConf(path):
    with open(path,"rb") as file:
        conf=json.load(file)
    return conf

def writeConf(path,conf):
    with open(path,"w") as file:
        json.dump(obj=conf,fp=file)
    return

def resetConf(path):
    conf={"seeni":1,"NOTSeeni":1}
    writeConf(path,conf)
    return
