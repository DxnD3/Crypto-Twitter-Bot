
import tweepy
from TwitterAPI import createAPI
import time
import requests
import json



key = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
api = createAPI()
def fetchPrice():
    price= requests.request(method='GET',url=key)
    price=price.json()
    price=json.dumps(price)
    return price[12:-8]
def main():
    a = True
    while a:
        btcPrice = fetchPrice()
        btcPrice = btcPrice.split(sep=" ")
        tweepy.API.update_status(api, status='#'+btcPrice[0].removesuffix('",')+' trading at: $'+btcPrice[2].removeprefix('"'))
        time.sleep(3600)
main()