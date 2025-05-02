from encoder import encode_string, save_to_file, generate_footer
from nacl.signing import SigningKey
from datetime import datetime, timezone

# 💬 Nachricht eingeben
message = input("💬 Nachricht eingeben: ")

# 📅 Zeitstempel (UTC mit Zeitzone)
timestamp = datetime.now(timezone.utc).isoformat()

# 🔧 ByteStruct-Felder
payload = bytearray()
payload.extend(encode_string(0x10, message))
payload.extend(encode_string(0x11, timestamp))

# 🔐 Schlüssel erzeugen & Footer generieren
signing_key = SigningKey.generate()
footer = generate_footer(payload, signing_key)

# 🧱 ByteStruct-Datei aufbauen
header = bytearray([0x01, 0x00])
final_data = header + payload + footer

# 💾 Speichern
save_to_file("message.bstruct", final_data)
with open("public.key", "wb") as f:
    f.write(signing_key.verify_key.encode())

print("✅ Nachricht gespeichert als: message.bstruct")
print("📤 Public Key gespeichert in: public.key")
