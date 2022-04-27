import requests
#using financialmodelingprep api

API_KEY = "014b3f934ae524503d4bfa9cbde9a230"
API_URL = "https://financialmodelingprep.com/api/v3/quote/{asset}USD?apikey={API_KEY}"
STOCK_API_URL = "https://financialmodelingprep.com/api/v3/quote-short/{asset}?apikey={API_KEY}"

def generate_stock_url(stock, api_key):
    new_url = STOCK_API_URL.format(asset = stock, API_KEY = api_key)
    return new_url

def generate_crypto_url(coin,api_key):
    new_url = API_URL.format(asset = coin,API_KEY = api_key)
    return new_url

def generate_price(url):
    response = requests.get(url)
    try:
        data = response.json()[0]
        price = data['price']
        return price
    except:
        return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    while True:
            user_in = input("Enter crypto or stock short name: ").upper()
            x = generate_price(user_in, API_KEY)
            print("{price}".format(price=generate_price(x)))