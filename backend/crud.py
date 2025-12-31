from sqlalchemy.orm import Session
from . import models, schemas

def get_osszes_adat(db: Session, limit: int = 100):
    return db.query(models.KriptoAdat).order_by(models.KriptoAdat.rogzites_ideje.desc()).limit(limit).all()


def adat_mentese(db: Session, adat: schemas.AdatLetrehozas):
    
    uj_sor = models.KriptoAdat(
        nev=adat.nev, 
        aktualis_ar=adat.aktualis_ar
    )
    
    db.add(uj_sor)     
    db.commit()        
    db.refresh(uj_sor)
    
    return uj_sor

def get_statisztika(db: Session):
    
    adatok = db.query(models.KriptoAdat).all()
    
    if not adatok:
        return {"atlag": 0, "max": 0, "min": 0}

    
    arak = list(map(lambda x: x.aktualis_ar, adatok))
    
   
    magas_arak = list(filter(lambda x: x > 28800000, arak))
    
    
    atlag = sum(arak) / len(arak)
    
    return {
        "atlag_ar_huf": round(atlag, 0),
        "maximum_ar": max(arak),
        "minimum_ar": min(arak),
        "20m_feletti_meresek_szama": len(magas_arak)
    }