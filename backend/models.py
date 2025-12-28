from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from .database import Base

class KriptoAdat(Base):
    __tablename__ = "kripto_arak"  

    id = Column(Integer, primary_key=True, index=True)
    nev = Column(String, index=True)     
    aktualis_ar = Column(Float)          
    rogzites_ideje = Column(DateTime(timezone=True), 
    server_default=func.now())