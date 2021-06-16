from fastapi import FastAPI 
from naruto import models
from naruto.database import engine
from naruto.routers import kage, akatsuki, villages


app = FastAPI()

models.Base.metadata.create_all(engine)

# @app.get("/country")
# async def show_country():
#     return "Country"
# app.include_router(kage.router)
app.include_router(kage.router)
app.include_router(akatsuki.router)
app.include_router(villages.router)