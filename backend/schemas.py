from pydantic import BaseModel
from datetime import datetime

class AdatBase(BaseModel):
    nev: str
    aktualis_ar: float

class AdatLetrehozas(AdatBase):
    pass

class AdatKiiratas(AdatBase):
    id: int
    rogzites_ideje: datetime

    class Config:
        from_attributes = True