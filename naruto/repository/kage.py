from starlette import status
from naruto import models
from sqlalchemy.orm import Session
from naruto.schemas import Kage
from fastapi import HTTPException


def show_all(db: Session):
    kage = db.query(models.KageModel).all()
    return kage


def create(request: Kage, db: Session):
    new_kage = models.KageModel(name=request.name, description=request.description, village_id=request.village_id)
    db.add(new_kage)
    db.commit()
    db.refresh(new_kage)
    return new_kage

def show(name, db: Session):
    
    # we get from name result like = "naruto" but in db it is "Naruto" and we converts the first character of the string to a capital (uppercase)
    name_ = name.capitalize()
    kage = db.query(models.KageModel).filter(models.KageModel.name == name_).first()
    if not kage:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Kage with the name ({name_}) not found")
    return kage