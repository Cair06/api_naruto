from fastapi import APIRouter, status, Depends
from ..schemas import Village, VillageForKage
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import villages
from typing import List

router = APIRouter(
    prefix="/village",
    tags=["Villages"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(request: VillageForKage, db: Session = Depends(get_db)):
    return villages.create(request, db)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[Village])
async def show_all(db: Session = Depends(get_db)):
    return villages.show_all(db)

@router.get("/{name}", response_model=Village)
def show(name, db: Session = Depends(get_db)):
    return villages.show(name, db)