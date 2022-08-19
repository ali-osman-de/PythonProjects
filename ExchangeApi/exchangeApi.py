
import requests

base_url = 'https://api.binance.com'

path = '/api/v3/exchangeInfo'

r = requests.get(base_url+path)

params = '?symbol=BTCUSDT&interval=1m'

r = requests.get(base_url+path,params={'symbol':'BTCUSDT','interval':'1m'})

print(r.json)