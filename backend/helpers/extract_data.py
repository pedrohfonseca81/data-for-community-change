import csv
import os
from typing import Any, Optional, Union

import requests


class csvParser:
    def __init__(self, filename) -> None:
        self.filename: str = filename
        self.data: dict[Any, Any] = {}

        data: list[dict] = self.load_data()
        self.process_data(data)

    def load_data(self) -> list[dict]:
        temp_data: list[dict] = []

        with open(f"{os.getcwd()}/reports/{self.filename}", encoding="utf-8") as csvfile:
            csvreader = csv.DictReader(csvfile, delimiter=";")
            for row in csvreader:
                temp_data.append(row)
        
        return temp_data

    def process_data(self, data: dict[Any, Any]) -> None:
        field: str
        for field in data:
            state: str = field["UF"]
            city: str = field["Município"]

            if not state in self.data:
                self.data[state] = {}
    
            if not city in self.data[state]:
                self.data[state][field["Protocolo"]] = {}

            self.data[state][field["Protocolo"]] = {
                #"protocol": field["Protocolo"],
                "COBRADE": field["COBRADE"],
                "status": field["Status"],
                "date": field["Registro"],
                #"population": field["População"],
                "dead": field["DH_Mortos"],
                "wounded": field["DH_Feridos"],
                "sick": field["DH_Enfermos"],
                "homeless": field["DH_Desabrigados"],
                "missing": field["DH_Desaparecidos"],
                "city" : {
                    "name": city,
                    "population": field["População"]
                }
            }

    def get_city_population(self, city: str) -> int:
        for cities in self.data.values():
            if city in cities:
                return int(cities[city]["city"]["population"])

        return "City not found"

    def get_state_population(self, state: str) -> int:
        state = state.upper()
        population: int = 0

        if state in self.data:
            for _, values in self.data[state].items():
                population += int(values["city"]["population"])

        return "State not found"

    def get_state_disasters(
        self,
        state: str,
        max_results: Optional[int] = None,
        order_by: Union[str, None] = None,
        coords: Optional[bool] = True
    ) -> dict[Any, Any]:
        state = state.upper()
        disasters = {}

        if state in self.data:
            for key, value in self.data[state].items():
                if max_results is not None:
                    max_results -= 1
                    if max_results <= -2:
                        break

                disasters[key] = value

        if order_by:
            disasters = dict(sorted(disasters.items(), reverse=True, key=lambda x: int(x[1][order_by])))

        if not coords:
            for city in disasters:
                disasters[city]["city"]["latitude"] = 0
                disasters[city]["city"]["longitude"] = 0
            return disasters

        req = requests.get(f"https://brasilapi.com.br/api/ibge/municipios/v1/{state}?providers=gov")
        city_list = req.json()

        for city in disasters:
            ibge_code = 0

            for cities in city_list:
                for key, value in cities.items():
                    if value.lower() == city.lower():
                        ibge_code = cities["codigo_ibge"]

            if ibge_code == 0:
                continue

            latitude, longitude = self.get_city_coords(ibge_code)
            disasters[city]["city"]["latitude"] = latitude
            disasters[city]["city"]["longitude"] = longitude
    
        return disasters
    
    @staticmethod
    def get_city_coords(ibge_code: int) -> list[int, int]:
        try:
            req = requests.get(f"https://servicodados.ibge.gov.br/api/v1/bdg/municipio/{ibge_code}/estacoes")
            json = req.json()
        except:
            return [0, 0]
    
        latitude = 0
        longitude = 0

        for key in json:
            if isinstance(key, dict):
                for k, v in key.items():
                    if k == "longitude":
                        longitude = v
                    elif k == "latitude":
                        latitude = v

        return [latitude, longitude]