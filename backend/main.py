import threading 
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, crud
from .database import SessionLocal, engine
from .services import scraper

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Kripto")


@app.on_event("startup")
def inditas():

    robot_szal = threading.Thread(target=scraper.adatgyujto_inditasa, daemon=True)
    robot_szal.start()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def nyito_oldal():
    return {"uzenet": "Működik a szerver!"}

@app.get("/adatok/", response_model=List[schemas.AdatKiiratas])
def adatok_listazasa(limit: int = 50, db: Session = Depends(get_db)):
    adatok = crud.get_osszes_adat(db, limit=limit)
    return adatok

@app.get("/statisztika/")
def statisztika_lekerese(db: Session = Depends(get_db)):
    
    stat = crud.get_statisztika(db)
    return stat