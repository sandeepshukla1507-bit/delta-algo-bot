import ccxt
import os

# GitHub Secrets से चाबियाँ उठाना
api_key = os.getenv('DELTA_API_KEY')
api_secret = os.getenv('DELTA_API_SECRET')

# डेल्टा इंडिया सेटअप (CCXT के जरिए)
exchange = ccxt.delta({
    'apiKey': api_key,
    'secret': api_secret,
})

def start_trading():
    try:
        # 1. कनेक्शन और बैलेंस चेक
        balance = exchange.fetch_balance()
        usdt_balance = balance['total'].get('USDT', 0)
        print(f"✅ कनेक्शन सफल! वर्तमान बैलेंस: {usdt_balance} USDT")
        
        # यहाँ हम आगे अपनी स्ट्रैटेजी लिखेंगे
        
    except Exception as e:
        print(f"❌ चूक हो गई: {e}")

if __name__ == "__main__":
    start_trading()
