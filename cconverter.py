import requests

cache = {'usd': requests.get('http://www.floatrates.com/daily/usd.json').json(),
         'eur': requests.get('http://www.floatrates.com/daily/eur.json').json()}


currency_code = input().lower().strip()
if currency_code != '':
    while True:
        new_amount = 0
        devise_code = input().lower().strip()
        if devise_code == '':
            break
        amount = int(input())
        print("Checking the cache…")
        if devise_code in cache:
            print("Oh! It is in the cache!")
            new_amount = amount / cache[devise_code][currency_code]['rate']
        else:
            print("Sorry, but it is not in the cache!")
            r = requests.get('http://www.floatrates.com/daily/' + devise_code + '.json')
            if r:
                try:
                    new_amount = amount / r.json()[currency_code]['rate']
                except IndexError:
                    pass
                else:
                    cache[devise_code] = r.json()

        print("You received.", round(new_amount, 2), devise_code.upper())
