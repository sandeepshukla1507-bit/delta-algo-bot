import os
import asyncio
import ccxt.async_support as ccxt

# GitHub Secrets से चाबियाँ उठाना
API_KEY = os.environ.get('DELTA_API_KEY')
API_SECRET = os.environ.get('DELTA_API_SECRET')

async def session_sniper():
    exchange = ccxt.delta({'apiKey': API_KEY, 'secret': API_SECRET})
    print("🚀 [GITHUB SNIPER] सेशन शुरू... मार्केट स्कैनिंग जारी है।")
    
    try:
        balance = await exchange.fetch_balance()
        print(f"💰 वॉलेट बैलेंस: ${balance['total'].get('USDT', 0):.2f} USDT\n")
        
        # 1 घंटे तक स्कैनिंग (GitHub Action की लिमिट बचाने के लिए)
        for _ in range(120): # हर 30 सेकंड में स्कैन, कुल 60 मिनट
            tickers = await exchange.fetch_tickers()
            for symbol, data in tickers.items():
                if 'USDT' in symbol and '-' not in symbol:
                    change = float(data['percentage'])
                    if abs(change) > 3.0:
                        print(f"🎯 [TARGET] {symbol} | मूव: {change}% | प्राइस: {data['last']}")
            await asyncio.sleep(30)
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    asyncio.run(session_sniper())
