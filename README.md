App Name: Smart Thermostat
===================

Flask Web-Anwendung die mit Arduino Kommuniziert.
===================

Um die Anwendung auszuführen:

1.  Python und Virtual Environment installieren, in Terminal:
    > python3 (Global! Auch Umgebungsvariablen setzen)
    > Im Verzeichniss rein gehen: Im gleichen Ordner wie diese Readme Datei -> mit "cd <Ordner-path>"
    > python -m venv venv                                       # Install Virtual Environment

2. Die Umgebung activieren:
    Windows:
    > venv\scripts\activate
    Mac / Linux: 
    > source venv/bin/activate

3.  Flask installieren
    > pip install flask

4. Die notwendigen Bibliotheken installieren
    > pip install -r requirements.txt

5.  Datenbank aufsetzten:
    > flask shell < init_db.py

6. Die Anwendung starten
    > set FLASK_APP=app.py					
    > set FLASK_DEBUG=1								
    > flask run

7. Im Browser die Adresse
    `http://localhost:5000`
    aufrufen.

8. Folgende Nutzer sind angelegt:
    > 'admin@example.com' Password: 'Password1'

9. Andere Nutzer kann der Admin hinzufügen

10.  Die Anwendung beenden:
    > strg+C
    > deactivate
    > exit oder quit

===================
Nutzliche Kommandos:

1. Die Anwendung speichert alles in die Datenbank data.sqlite:
    > flask db init (Nur das erste Mal! -> Schon gemacht!)
    > flask db migrate -m "Migration"
    > flask db upgrade
    > Migration-Folder ist schon angelegt

2. Setze den Secret Key:
    > Secret Key ist schon gesetzt mit: set SECRET_KEY=ThermostatAPP

    
===================
AUTHOREN: Milana Popovic, Sara Amorosa und Claudia Silva