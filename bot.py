import ccxt
import time

# --- कॉन्फ़िगरेशन (अपनी डिटेल्स यहाँ भरें) ---
DELTA_INDIA_KEY = 'G5BKW96b618DyspZs9rFrc3vAgufyP'
DELTA_INDIA_SECRET = 'kidjjgCPjFmtWRNPqTX2wZP0rySxZgchGQ9wBFzl3FamrolASpqDfHCMAX5N'

# --- CCXT पावर सेटअप ---
exchange = ccxt.delta({
    'apiKey': DELTA_INDIA_KEY,
    'secret': DELTA_INDIA_SECRET,
    'enableRateLimit': True,  # ताकि एक्सचेंज आपको ब्लॉक न करे
    'urls': {
        'api': {
            'public': 'https://api.india.delta.exchange',
            'private': 'https://api.india.delta.exchange',
        }
    },
    # 💡 IP PROBLEM SOLUTION: अगर आपके पास Static Proxy है, तो यहाँ डालें
    # 'proxies': {
    #     'http': 'http://username:password@proxy_address:port',
    #     'https': 'http://username:password@proxy_address:port',
    # },
})

def start_bot():
    print("🚀 संदीप का अल्गो बॉट शुरू हो रहा है...")
    
    try:
        # 1. बैलेंस चेक करना (सबसे आसान तरीका)
        balance = exchange.fetch_balance()
        usdt_balance = balance['total'].get('USDT', 0)
        print(f"💰 आपका डेल्टा इंडिया बैलेंस: {usdt_balance} USDT")

        # 2. मार्केट प्राइस चेक करना (BTC/USDT)
        ticker = exchange.fetch_ticker('BTC/USDT')
        print(f"📈 BTC की ताज़ा कीमत: ${ticker['last']}")

        # 3. ओपन ऑर्डर्स देखना
        open_orders = exchange.fetch_open_orders()
        print(f"📂 आपके ओपन ऑर्डर्स की संख्या: {len(open_orders)}")

    except Exception as e:
        print(f"❌ अरे! एरर आ गया: {e}")
        print("💡 सुझाव: डेल्टा सेटिंग्स में जाकर अपनी Current IP को 'Whitelist' करें।")

if __name__ == "__main__":
    # बॉट को हर 30 सेकंड में चलाने के लिए (लूप)
    while True:
        start_bot()
        print("Waiting for 30 seconds...")
        time.sleep(30)
