from web3 import Web3
import sys
import json
#import config
import time
from datetime import datetime
import pytz

data=json.loads(sys.argv[1])

my_wallet = data["my_wallet"]

export = {}
count=0
balance=0
humanReadable=0

while True:
    try:
        bsc = "https://bsc-dataseed.binance.org/"
        web3 = Web3(Web3.HTTPProvider(bsc))
        balance = web3.eth.get_balance(my_wallet)
        humanReadable = web3.fromWei(balance,'ether')
        export["humanReadable"]=(str(humanReadable))

    except:
        count = count +1

    
    if humanReadable > 0:
        break

    if count > 10:
        break




print(json.dumps(export))
