# Car REST API 🚗

Eine einfache REST-API zur Verwaltung von Fahrzeugdaten, entwickelt mit **Python** und **FastAPI**.

## Endpunkte

* **GET `/cars`** – Alle Autos abrufen
* **GET `/cars/{car_id}`** – Einzelnes Auto anhand der ID abrufen
* **POST `/cars`** – Neues Auto hinzufügen
* **PUT `/cars/{car_id}`** – Fahrzeugdaten aktualisieren
* **DELETE `/cars/{car_id}`** – Auto löschen

## Lokale Installation & Start

1. Repository klonen oder herunterladen.
2. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
