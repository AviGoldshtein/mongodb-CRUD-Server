from fastapi import FastAPI
from services.dal.dal import DataLoader
from pydantic import BaseModel

from services.helpers.convertor import convert_bson_types

class Soldier(BaseModel):
    ID: int
    first_name: str
    last_name: str
    phone_number: int
    rank: str

app = FastAPI()
dal = DataLoader()

@app.get("/")
def health():
    return {"health": "working"}

@app.get("/all_soldiers")
def get_all_soldiers():
    result = dal.get_all_soldiers()
    return convert_bson_types(result)

@app.post("/insert_soldier")
def insert_soldier(solder: Soldier):
    return dal.insert_soldier(
        ID=solder.ID,
        first_name=solder.first_name,
        last_name=solder.last_name,
        phone_number=solder.phone_number,
        rank=solder.rank
    )

