from sqlalchemy import Column, Integer, String, ForeignKey
from naruto.database import Base
from sqlalchemy.orm import relationship


class KageModel(Base):
    __tablename__="kage"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    
    village_id = Column(Integer, ForeignKey("villages.id"))
    village = relationship("VillageModel", back_populates="kage")

class AkatsukiModel(Base):
    __tablename__="akatsuki"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    
class VillageModel(Base):
    __tablename__="villages"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    kage = relationship("KageModel", back_populates="village")
