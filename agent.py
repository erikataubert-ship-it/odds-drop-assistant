import requests
import time

BOT_TOKEN = "IDE_A_BOT_TOKEN"
CHAT_ID = "IDE_A_CHAT_ID"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": msg
    }
    requests.post(url, data=data)

# SZIMULÁLT odds adatok (később cseréljük élőre)
matches = [
    {"match": "Team A vs Team B", "market": "Over 2.5", "old": 2.10, "new": 1.82},
    {"match": "Team C vs Team D", "market": "Over 3.5", "old": 2.40, "new": 2.35},
    {"match": "Team E vs Team F", "market": "Over 2.5", "old": 1.95, "new": 1.60}
]

def detect_drop():
    alerts = []

    for m in matches:
        drop = m["old"] - m["new"]

        if drop >= 0.20:
            alerts.append(m)

    return alerts

def run():
    drops = detect_drop()

    if not drops:
        send_telegram("📡 Odds figyelő: nincs jelentős mozgás")
        return

    for d in drops:
        msg = f"""
📉 ODDS DROP

{d['match']}
{d['market']}

{d['old']} ➜ {d['new']}

Piaci pénz érkezett ⚠️
"""
        send_telegram(msg)

if __name__ == "__main__":
    run()
