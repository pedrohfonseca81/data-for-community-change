from typing import Any, Optional, Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from helpers.extract_data import csvParser
from repository import Repository

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

parser = csvParser("datas.csv")
repository = Repository(parser)


@app.get("/city-population")
def population_by_city(city: str) -> Union[int, str]:
    return repository.get_city_population(city)

@app.get("/state-population")
def population_by_state(state: str) -> Union[int, str]:
    state = state.upper()
    return repository.get_state_population(state)

@app.get("/state-disasters")
def disasters_by_state(
    uf: str,
    state: str,
    max_results: Optional[int] = None,
    order_by: Union[str, None] = None,
    coords: Optional[bool] = True
) -> dict[Any, Any]:
    state = state.upper()
    return repository.get_state_disasters(uf, state, max_results, order_by, coords)

@app.get("/city-info")
def get_city_info(city: str):
    return repository.get_city_info(city)