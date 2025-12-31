A rendszer célja, hogy manuális beavatkozás nélkül, folyamatosan gyűjtse a kriptovaluta piaci adatokat (általam megadott jelenlegi piaci érték alapján, nem pedig egy bróker api-ból gyűjti az adatokat), azokból statisztikát készítsen (átlag, minimum, maximum számítás), és az eredményeket egy könnyen értelmezhető, grafikonokkal ellátott webes felületen tálalja.

Felépítés:

1. Adatgyűjtő (Scraper): Egy háttérfolyamat, amely 10 másodpercenként lekéri a friss adatokat a Coinbase nyilvános felületéről.

2. Backend (API): Python nyelven, FastAPI keretrendszerrel készült szerver, amely az adatok mentéséért és a statisztikai számításokért felel.

3. Adatbázis: SQLite relációs adatbázis, amely strukturáltan tárolja a méréseket (id, nev, ar, időpont).

4. Frontend: Streamlit alapú webes felület, amely a felhasználó számára vizualizálja az adatokat.

Teljes rendszer gyors indítása: python start.py
Ez a szkript automatikusan elindítja a FastAPI szervert a háttérben, vár a kapcsolat létrejöttére, majd megnyitja a Streamlit felületet.(ha nem tölt be az adat, a terminálból kapott linket nyissuk meg)

Frontend: https://bitcoinarfolyam.streamlit.app/

Backend: https://lfckw8-multi-beadand.onrender.com


