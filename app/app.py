from fastapi import FastAPI
from services.dal.dal import DataLoader

app = FastAPI()
data_loader = DataLoader()

@app.get("/")
def get_data():
    return {"health": "working"}