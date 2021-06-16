from pydantic import BaseModel
from typing import List, Optional

             
class Akatsuki(BaseModel):
    name: str
    description: str
    class Config:
        orm_mode = True


class Kage(BaseModel):
    name: str
    description: str
    village_id: int
    class Config:
        orm_mode = True

        
class KageForVillage(BaseModel):
    name: str
    class Config:
        orm_mode = True

            
class Village(BaseModel):
    name: str
    kage: List[KageForVillage] = []
    class Config:
        orm_mode = True

class VillageForKage(BaseModel):
    name: str
    class Config:
        orm_mode = True
        
class KageShow(BaseModel):
    name: str
    description: str
    village: VillageForKage
    class Config:
        orm_mode = True