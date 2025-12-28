import time         
import threading    
import random
from .. import models, database


def random_ar_generalas():
    alap_ar = 28800000.0
    valtozas = random.uniform(-50000, 50000) 
    return alap_ar + valtozas


def adatgyujto_inditasa():
    print("Háttérfolyamat elindult")
    
    while True:
        try:
          
            db = database.SessionLocal()
            
            jelenlegi_ar = random_ar_generalas()
            
            uj_adat = models.KriptoAdat(nev="BTC", aktualis_ar=jelenlegi_ar)
            db.add(uj_adat)
            db.commit()
            
            print(f"Új ár: {jelenlegi_ar:,.0f} Ft")
            
            db.close()
            
        except Exception as e:
            print(f"Hiba: {e}")
            
        time.sleep(10)