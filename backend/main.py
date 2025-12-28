import logging
import threading
from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import SessionLocal, engine
from .services import scraper


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Kripto Beadando")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def inditas():
    logger.info("Rendszer indítása...")
    
    robot_szal = threading.Thread(target=scraper.adatgyujto_inditasa, daemon=True)
    robot_szal.start()
    
    logger.info("Scraper elindult.")
    logger.info("A Backend szerver megy.")


@app.get("/")
def nyito_oldal():
    return {"uzenet": "Szerver:", "status": "OK"}

@app.get("/adatok/", response_model=List[schemas.AdatKiiratas])
def adatok_listazasa(limit: int = 50, db: Session = Depends(get_db)):
 
    adatok = crud.get_osszes_adat(db, limit=limit)
    return adatok

@app.get("/statisztika/")
def statisztika_lekerese(db: Session = Depends(get_db)):

    adatok = crud.get_osszes_adat(db, limit=1000)
    
    if not adatok:
        return {"uzenet": "Nincs elég adat a statisztikához"}

    arak = list(map(lambda x: x.aktualis_ar, adatok))
    
    magas_arak = list(filter(lambda x: x > 100, arak))

    atlag = sum(arak) / len(arak)

    return {
        "elemszam": len(arak),
        "atlag_ar": round(atlag, 2),
        "maximum_ar": max(arak),
        "minimum_ar": min(arak),
        "magas_aruak_szama": len(magas_arak)
    }