from typing import Any, Optional, Union
from datetime import datetime
import requests
import os

import dotenv


class Repository:
    def __init__(self, parser) -> None:
        self.parser = parser

        self.data: dict[Any, Any] = parser.process_data(parser.load_data())

        dotenv.load_dotenv(override=True)

    def get_city_population(self, city: str) -> int:
        for cities in self.data.values():
            if city in cities:
                return int(cities[city]["city"]["population"])

        return "City not found"

    def get_state_population(self, state: str) -> int:
        population: int = 0

        if state in self.data:
            for _, values in self.data[state].items():
                population += int(values["city"]["population"])

        return "State not found"

    def get_state_disasters(
        self,
        uf: str,
        state: str,
        max_results: Optional[int] = None,
        order_by: Union[str, None] = None,
        coords: Optional[bool] = True
        
    ) -> dict[Any, Any]:
        disasters = {}
        all_disasters = {}

        if uf in self.data:
            for key, value in self.data[uf].items():
                all_disasters[key] = value

        if order_by:
            all_disasters = dict(sorted(all_disasters.items(), reverse=True, key=lambda x: int(x[1][order_by])))
        
        if max_results is not None:
            for key, value in all_disasters.items():
                    max_results -= 1
                    if max_results <= -2:
                        break

            disasters[key] = value

        if not coords:
            for city in disasters:
                disasters[city]["city"]["latitude"] = 0
                disasters[city]["city"]["longitude"] = 0
            return disasters

        # req = requests.get(f"https://brasilapi.com.br/api/ibge/municipios/v1/{uf}?providers=gov")
        # city_list = req.json()

        for protocol, info in disasters.items():
            # ibge_code = 0
            # for cities in city_list:
            #     for key, value in cities.items():
            #         if value.lower() == city.lower():
            #             ibge_code = cities["codigo_ibge"]
            # if ibge_code == 0:
            #     continue

            disasters[protocol]["city"]["info"] = self.get_city_coords(f"{info['city']['name']} {state}")
    
        return disasters

    def get_city_info(self, city: str):
        coords = self.get_city_coords(city)

        if isinstance(coords, str):
            return coords
            
        return {
            "temperature": self.get_city_temperature(coords["latitude"], coords["longitude"]),
            "coordinates": coords
        }

    def get_city_temperature(self, latitude: int, longitude: int):
        now = datetime.now()

        try:
            req = requests.get(f"https://api.meteomatics.com/{now.strftime('%Y-%m-%dT%H:%M:00Z')}/t_2m:C/{latitude},{longitude}/json?access_token={os.getenv('access_token')}")
            req = req.json()
        except:
            return 0

        return req["data"][0]["coordinates"][0]["dates"][0]["value"]

    @staticmethod
    def get_city_coords(city: str):
        req = requests.get(f"https://photon.komoot.io/api/?q={city}&limit=1")
        req = req.json()

        try:
            coords  = req["features"][0]["geometry"]["coordinates"]
        except IndexError:
            return "Invalid city name"

        return {
            "longitude": coords[0],
            "latitude": coords[1],
            "properties": {
                "name": req["features"][0]["properties"]["name"],
                "state": req["features"][0]["properties"]["country"],
                "country": req["features"][0]["properties"]["country"]
                #"extent": req["features"][0]["properties"]["extent"]
            }
        }

    # Unused - rate limited
    @staticmethod
    def get_city_coords_open_street_map(state: str, city: str, geojson: bool = False):
        req = requests.get(f"https://nominatim.openstreetmap.org/search.php?city={city}&state={state}&polygon_geojson=1&countrycodes=BR&format=jsonv2")
        req = req.json()

        city_dict = req[0]

        return {
            "longitude": city_dict["lon"],
            "latitude": city_dict["lat"],
            "geojson": city_dict["geojson"] if geojson else None
        }
    
    # Slow
    @staticmethod
    def get_city_coords_ibge(ibge_code: int) -> list[int, int]:
        try:
            req = requests.get(f"https://servicodados.ibge.gov.br/api/v1/bdg/municipio/{ibge_code}/estacoes")
            json = req.json()
        except:
            return [0, 0]
    
        latitude: int = 0
        longitude: int = 0

        for key in json:
            if isinstance(key, dict):
                for k, v in key.items():
                    if k == "longitude":
                        longitude = v
                    elif k == "latitude":
                        latitude = v

        return [latitude, longitude]