import requests, time

def avalanche_sniper():
    print("Avalanche C-Chain — instant new token + liquidity sniper")
    seen = set()
    while True:
        r = requests.get("https://api.snowtrace.io/api?module=account&action=txlistinternal&address=0xA7D7079b0FEaD91F3e65f86E8915Cb59&sort=desc")
        for tx in r.json().get("result", [])[:25]:
            txid = tx["hash"]
            if txid in seen or "Liquidity" not in tx.get("input", ""): continue
            seen.add(txid)
            value = int(tx["value"]) / 1e18
            if value > 5:  # >5 AVAX liquidity add
                print(f"LIQUIDITY ADDED on AVAX!\n"
                      f"Value: {value:.2f} AVAX (~${value*35:,.0f})\n"
                      f"Contract: {tx['to']}\n"
                      f"Tx: https://snowtrace.io/tx/{txid}\n"
                      f"→ New TraderJoe / Pangolin pool just went live!\n"
                      f"Check: https://dexscreener.com/avalanche/{tx['to']}\n"
                      f"{'❄️🔥'*20}")
        time.sleep(2.2)

if __name__ == "__main__":
    avalanche_sniper()
