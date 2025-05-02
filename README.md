# 💬 ByteStructChat – Demo

Mini-Chat-Demo zur Demonstration von ByteStruct mit digital signierten Nachrichten.

Dieses Projekt demonstriert, wie strukturierte, binäre Daten mit einer digitalen Signatur gesichert und verifiziert werden können. Die Anwendung besteht aus einem Mini-Chat, bei dem jede Nachricht als .bstruct gespeichert und gegen Manipulation geschützt wird.

## 🚀 Installation

```bash
git clone https://github.com/ribershamoelias/ByteStructChat.git
cd ByteStructChat
pip install -r requirements.txt
pip install -e ../ByteStruct  # Falls ByteStruct im Nachbarverzeichnis liegt
```
## 📨 Nachricht senden
```bash
python send_message.py
```
Gibt: message.bstruct + public.key
## 📩 Nachricht empfangen & prüfen
```bash
python receive_message.py
```
Gibt:

Inhalt der Nachricht

Signaturstatus

✅ Wenn alles korrekt: "Signatur ist GÜLTIG"

## 🔐 Benötigte Pakete

- pynacl

- dein ByteStruct-Projekt (lokal installiert)
