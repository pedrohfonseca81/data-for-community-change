from typing import Any, Optional, Union

from fastapi import FastAPI

from helpers.extract_data import csvParser

app = FastAPI()
parser = csvParser("datas.csv")

@app.get("/city-population")
def population_by_city(city: str) -> Union[int, str]:
    return parser.get_city_population(city)

@app.get("/state-population")
def population_by_state(state: str) -> Union[int, str]:
    return parser.get_state_population(state)

@app.get("/state-disasters")
def disasters_by_state(
    state: str,
    max_results: Optional[int] = None,
    order_by: Union[str, None] = None,
    coords: Optional[bool] = True
) -> dict[Any, Any]:
    return parser.get_state_disasters(state, max_results, order_by, coords)

# Example
# @app.get("/items/{item_id}")
# def get_item(item_id: int, query: Union[str, None] = None):
#     return {"item_id": item_id, "query": query}
