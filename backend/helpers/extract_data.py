import csv
import os
from typing import Any


class csvParser:
    def __init__(self, filename) -> None:
        self.filename: str = filename

        data: list[dict] = self.load_data()
        self.process_data(data)

    def load_data(self) -> list[dict]:
        temp_data: list[dict] = []

        with open(f"{os.getcwd()}/reports/{self.filename}", encoding="utf-8") as csvfile:
            csvreader = csv.DictReader(csvfile, delimiter=";")
            for row in csvreader:
                temp_data.append(row)
        
        return temp_data

    @staticmethod
    def process_data(data: list[dict]) -> dict[Any, Any]:
        field: str
        processed_data: dict[Any, Any] = {}

        for field in data:
            state: str = field["UF"]
            city: str = field["Município"]

            if not state in processed_data:
                processed_data[state] = {}
    
            if not city in processed_data[state]:
                processed_data[state][field["Protocolo"]] = {}

            processed_data[state][field["Protocolo"]] = {
                "COBRADE": field["COBRADE"],
                "status": field["Status"],
                "date": field["Registro"],
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

        return processed_data
