import os
def getConfig():
    config={}
    with open(".config","r") as f:
        config=eval(f.read())
    return config
