import os
import requests
from datetime import datetime

# Le tue credenziali aggiornate
TOKEN = "8632461457:AAEQBSFg0_mT3yo-f9QOJ4zkR48ukXcWkW0"
CHAT_ID = "46981666"

# Database della dieta (Dal 21 al 30 Settembre 2026)
dieta = {
    "2026-09-21": {"cena": "Protein + 300g Vegetable", "pranzo_domani": "90g Pasta/Riso + Protein + 300g Vegetable"},
    "2026-09-22": {"cena": "Protein + 300g Vegetable", "pranzo_domani": "90g Pasta/Riso + Protein + 300g Vegetable"},
    "2026-09-23": {"cena": "Protein + 300g Vegetable", "pranzo_domani": "90g Pasta/Riso + Protein + 300g Vegetable"},
    "2026-09-24": {"cena": "Protein + 300g Vegetable", "pranzo_domani": "90g Pasta/Riso + Protein + 300g Vegetable"},
    "2026-09-25": {"cena": "Protein + 300g Vegetable", "pranzo_domani": "90g Pasta/Riso + Protein + 300g Vegetable"},
    "2026-09-26": {"cena": "Protein + 300g Vegetable", "pranzo_domani": "90g Pasta/Riso + Protein + 300g Vegetable"},
    "2026-09-27": {"cena": "Protein + 300g Vegetable", "pranzo_domani": "90g Pasta/Riso + Protein + 300g Vegetable"},
    "2026-09-28": {"cena": "Protein + 300g Vegetable", "pranzo_domani": "90g Pasta/Riso + Protein + 300g Vegetable"},
    "2026-09-29": {"cena": "Protein + 300g Vegetable", "pranzo_domani": "90g Pasta/Riso + Protein + 300g Vegetable"},
    "2026-09-30": {"cena": "Protein + 300g Vegetable", "pranzo_domani": "Ultimo giorno del piano!"}
}

def invia_messaggio():
    oggi = datetime.now().strftime("%Y-%m-%d")
    
    # Prende i dati di oggi o un testo di fallback se la data non è in lista
    pasti = dieta.get(oggi, {"cena": "Protein + 300g Vegetable", "pranzo_domani": "90g Pasta/Riso"})
    
    testo = f"🤖 *Promemoria Dieta del Giorno*\n\n📅 Data: {oggi}\n\n🍽️ *Cena di stasera:* {pasti['cena']}\n🍱 *Pranzo di domani:* {pasti['pranzo_domani']}"
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": testo,
        "parse_mode": "Markdown"
    }
    
    response = requests.post(url, json=payload)
    print(response.json())

if __name__ == "__main__":
    invia_messaggio()