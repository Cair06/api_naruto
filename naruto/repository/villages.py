from starlette import status
from naruto import models
from sqlalchemy.orm import Session
from naruto.schemas import Village
from fastapi import HTTPException


def show_all(db: Session):
    village = db.query(models.VillageModel).all()
    return village


def create(request: Village, db: Session):
    new_village = models.VillageModel(name=request.name)
    db.add(new_village)
    db.commit()
    db.refresh(new_village)
    return new_village

def show(name, db: Session):
    village = db.query(models.VillageModel).filter(models.VillageModel.name == name).first()
    if not village:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Village with the name ({name}) not found")
    return village