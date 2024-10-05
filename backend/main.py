from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def get_item(item_id: int, query: Union[str, None] = None):
    return {"item_id": item_id, "query": query}

