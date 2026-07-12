import requests

def get_eth_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    try:
        response = requests.get(url).json()
        price = response['ethereum']['usd']
        print(f"Current ETH Price: ${price}")
    except Exception as e:
        print("Error fetching price:", e)

if __name__ == "__main__":
    print("Base Network Monitor Tool")
    get_eth_price()