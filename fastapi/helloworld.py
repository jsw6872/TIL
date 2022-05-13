from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, params: Optional[str] = None): # Optional는 Query
    return {"item_id": item_id, "param": params}