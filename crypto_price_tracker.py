import requests
import time

def get_crypto_price(crypto_id="bitcoin", currency="usd"):
    """Fetch the real-time price of a cryptocurrency from CoinGecko API"""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={currency}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        price = response.json()[crypto_id][currency]
        return price
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def track_prices(crypto_list, currency="usd", interval=10):
    """Continuously track crypto prices"""
    while True:
        print("\n--- Live Crypto Prices ---")
        for crypto in crypto_list:
            price = get_crypto_price(crypto, currency)
            if price is not None:
                print(f"{crypto.capitalize()} price: {price} {currency.upper()}")
        
        print("\nUpdating in", interval, "seconds...\n")
        time.sleep(interval)

if __name__ == "__main__":
    cryptos = ["bitcoin", "ethereum", "dogecoin"]  # Add more as needed
    track_prices(cryptos)