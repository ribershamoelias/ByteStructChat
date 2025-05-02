import os

print("📥 Empfangene Nachricht analysieren...\n")

# Schritt 1: Dekodieren
os.system("bstruct decode --input message.bstruct --pretty")

# Schritt 2: Verifikation
os.system("bstruct verify --input message.bstruct")
