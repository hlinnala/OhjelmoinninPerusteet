# Copyright (c) 2025 Henna Linnala
# License: MIT

from datetime import datetime, date
from typing import List, Dict

def muunna_tiedot(sahko: list) -> list:
    """Muuttaa tietojen tietotyyppiä"""
    muutettu_tieto = []
    muutettu_tieto.append(datetime.fromisoformat(sahko[0]))
    muutettu_tieto.append(int(sahko[1]))
    muutettu_tieto.append(int(sahko[2]))
    muutettu_tieto.append(int(sahko[3]))
    muutettu_tieto.append(int(sahko[4]))
    muutettu_tieto.append(int(sahko[5]))
    muutettu_tieto.append(int(sahko[6]))
    return muutettu_tieto

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

def suomalainen_pvm(aika: datetime) -> str:
    """Muuttaa datetime suomalaiseen muotoon pv.kk.vuosi"""
    suom_pvm = f"{aika.day}.{aika.month}.{aika.year}"
    return suom_pvm

def paivittainen_data(paiva: date, sahkodata: list) -> list:
    kulutus = [0, 0, 0]
    tuotanto = [0, 0, 0]
    for data in sahkodata:
        if data[0].date() == paiva:
            kulutus[0] += data[1] / 1000 
            kulutus[1] += data[2] / 1000
            kulutus[2] += data[3] / 1000
            tuotanto[0] += data[4] / 1000
            tuotanto[1] += data [5] / 1000
            tuotanto[2] += data[6] / 1000

    return [f"{kulutus[0]:.2f}".replace(".", ","),
            f"{kulutus[1]:.2f}".replace(".", ","),
            f"{kulutus[2]:.2f}".replace(".", ","),
            f"{tuotanto[0]:.2f}".replace(".", ","),
            f"{tuotanto[1]:.2f}".replace(".", ","),
            f"{tuotanto[2]:.2f}".replace(".", ",")]

#def main():
# kulutus_tuotanto_viikko41 = lue_data("viikko41.csv")
# kulutus_tuotanto_viikko42 = lue_data("viikko42.csv")
# kulutus_tuotanto_viikko43 = lue_data("viikko43.csv")

#with open("yhteenveto.txt", "w", encoding="utf-8") as f:
#    f.write(viikko41)
#    f.write(viikko42)
#    f.write(viikko43)


#if __name__ == "__main__":
#    main()