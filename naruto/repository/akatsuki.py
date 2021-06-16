from starlette import status
from naruto import models
from sqlalchemy.orm import Session
from naruto.schemas import Akatsuki
from fastapi import HTTPException


def show_all(db: Session):
    akatsuki = db.query(models.AkatsukiModel).all()
    return akatsuki


def create(request: Akatsuki, db: Session):
    new_akatsuki = models.AkatsukiModel(name=request.name, description=request.description)
    db.add(new_akatsuki)
    db.commit()
    db.refresh(new_akatsuki)
    return new_akatsuki

def show(name, db: Session):
    name_ = name.capitalize()
    akatsuki = db.query(models.AkatsukiModel).filter(models.AkatsukiModel.name == name_).first()
    if not akatsuki:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Member of 'Akatsuki' with the name ({name}) not found")
    return akatsuki
