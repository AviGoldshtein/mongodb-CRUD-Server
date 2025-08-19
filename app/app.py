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

class UpdateSolderRequest(BaseModel):
    ID: int
    field: str
    value: str

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

@app.put("/update_soldier")
def update_soldier(details: UpdateSolderRequest):
    return dal.update_soldier(
        ID=details.ID,
        field=details.field,
        value=details.value
    )

@app.delete("/delete_soldier/{ID}")
def delete_soldier(ID: int):
    return dal.delete_soldier(ID=ID)