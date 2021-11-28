# BSC---buy-approve-and-sell

## check-price.py
  check the price of a crypto currency
  ```
  run the command: check-price.py 0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82
  ```
  the script responds with a json:
  ```
  {"token": "0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82", "priceBNB": "0.02210641334400920900", "priceUSDT": "13.24012392723865220066"}
```













## buy.py
  Buy crypto currency
  run the command: 
  ```
  python3 /test/buy.py {
                    "token":"0xfb1a34eb2585b0ad7976420d7a21ef2f4aebeeb6",
                    "amount":"0.1",
                    "op":"buy",
                    "real":"0",
                    "my_wallet":"MY WALLER ADRESS",
                    "my_secret":"MY SECRET",
                    "gasPrice":"7"
                    }
  ```
 the script responds with a json with all the transaction information

  
  
  
  
  
  
  
  
  
## approve.py
  Approve a crypto currency before selling it
  
  run the command: 
  ```
  python3 /test/approve.py {
                              "token":"0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82",
                              "op":"approve",
                              "real":"0",
                              "my_wallet":"MY WALLER ADRESS",
                              "my_secret":"MY SECRET",
                              "gasPrice":"5"
                           }
  ```
  the script responds with a json with all the transaction information











  
## sell.py
  Sell crypto currency
  run the command: 
  ```
  python3 /test/sell.py {
                    "token":"0xfb1a34eb2585b0ad7976420d7a21ef2f4aebeeb6",
                    "amount":"0.1",
                    "op":"sell",
                    "real":"0",
                    "my_wallet":"MY WALLER ADRESS",
                    "my_secret":"MY SECRET",
                    "gasPrice":"7"
                    }
  ```
 the script responds with a json with all the transaction information

  
