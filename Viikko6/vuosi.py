# Copyright (c) 2025 Henna Linnala
# License: MIT
# #tsiisus mikä määrä dataa

from datetime import datetime, date
from typing import List, Dict

def muunna_tiedot(sahko: list) -> list:
    """Muuttaa tietojen tietotyyppiä"""

def sahkonkulutus_ja_tuotanto(data: str) -> List:
    """Lukee CSV-tiedoston ja palauttaa rivit
    Next(f) poistaa esittelytiedon"""
    sahkodata = []
    with open(data, "r", encoding="utf-8") as f:
        next(f) 
        for sahko in f:
            sahko = sahko.strip()
            sahkon_tiedot = sahko.split(';')
            sahkodata.append(muunna_tiedot(sahkon_tiedot))
    return sahkodata

def paivittainen_data(paiva: date, sahkodata: list) -> list:
    """Uusi data tulossa pitää käydä läpi, mitä siellä onkaan"""

def suomalainen_pvm(paiva: date):
    """Muuttaa päivämäärän muotoilun suomalaiseen muotoon (pv.kk.vuosi)"""
    suom_pvm= f"{paiva.day}.{paiva.month}.{paiva.year}"
    return suom_pvm

def main():
    "Ohjelman pääfunktio "

if __name__ == "__main__":
    main()