



import requests
import json

url = "https://api.apilayer.com/fixer/convert?to={0}&from={1}&amount={2}"


from_currency = input("Satılan döviz cinsi giriniz: ")

to_currency = input("Alınan döviz cinsi: ")

value = int(input(f"Ne kadar {to_currency} alacaksınız: "))

url = url.format(from_currency,to_currency,str(value))


payload = {}
headers= {
  "apikey": "36IwPSaJ4fmanzBIcrQ1Pwn1dinlDSef"
}

response = requests.request("GET", url, headers=headers, data = payload)


status_code = response.status_code
result = json.loads(response.text)

print(str(value) + " " + from_currency + " = " + str(result['result']) + " " + to_currency)
