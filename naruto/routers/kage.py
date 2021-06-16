from fastapi import APIRouter, status, Depends
from ..schemas import Kage, KageShow
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import kage
from typing import List

router = APIRouter(
    prefix="/kage",
    tags=["Kage"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(request: Kage, db: Session = Depends(get_db)):
    return kage.create(request, db)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[KageShow])
async def show_all(db: Session = Depends(get_db)):
    return kage.show_all(db)

@router.get("/{name}", response_model=KageShow)
def show(name, db: Session = Depends(get_db)):
    return kage.show(name, db)