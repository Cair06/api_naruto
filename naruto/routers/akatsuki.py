from fastapi import APIRouter, status, Depends
from ..schemas import Akatsuki
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import akatsuki
from typing import List


router = APIRouter(
    prefix="/akatsuki",
    tags=["Akatsuki"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(request: Akatsuki, db: Session = Depends(get_db)):
    return akatsuki.create(request, db)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[Akatsuki])
async def show_all(db: Session = Depends(get_db)):
    return akatsuki.show_all(db)

@router.get("/{name}")
def show(name, db: Session = Depends(get_db)):
    return akatsuki.show(name, db)