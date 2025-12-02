# Copyright (c) 2025 Henna Linnala
# License: MIT
from datetime import datetime, date
from typing import List, Dict

def muunna_tiedot(sahko: list) -> list:
    muutettu_tieto = []
    muutettu_tieto.append(datetime.fromisoformat(sahko[0]))
    muutettu_tieto.append(int(sahko[1]))
    muutettu_tieto.append(int(sahko[2]))
    muutettu_tieto.append(int(sahko[3]))
    muutettu_tieto.append(int(sahko[4]))
    muutettu_tieto.append(int(sahko[5]))
    muutettu_tieto.append(int(sahko[6]))
    return muutettu_tieto

def sahkonkulutus_ja_tuotanto(data: str) -> list:
# """Lukee CSV-tiedoston ja palauttaa rivit sopivassa rakenteessa."""
    sahkodata = []
    with open(data, "r", encoding="utf-8") as f:
        next(f) #Ottaa sarakeiden esittelytiteo pois
        for sahko in f:
            sahko = sahko.strip()
            sahkon_tiedot = sahko.split(';')
            sahkodata.append(muunna_tiedot(sahkon_tiedot))
    return sahkodata

#def hae_paiva(sahkodata: list[str]) -> datetime:
    #paivamaara = datetime.strptime(sahkodata[0], "%Y-%m-%d").date()
    #suomalainenpvm = paivamaara.strftime("%d.%m.%Y")
    #return suomalainenpvm

def paivittainen_data(paiva: date, sahkodata: list) -> list:
    kulutus = [0, 0, 0]
    tuotanto = [0, 0, 0]
    for data in sahkodata:
        if data[0].date() == paiva:
            kulutus[0] +- data[1]
            kulutus[1] +- data[2]


#def muutos(data: list):
    #/1000
    #kulutusdata/1000
    #kulutusdata/1000
    #tuotanto/1000
    #tuotanto/1000
    #tuotanto/1000

def main():
    sahkodata = sahkonkulutus_ja_tuotanto("viikko42.csv")
    """Ohjelman pääfunktio: lukee datan, laskee yhteenvedot ja tulostaa raportin."""
    print("\n\tViikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)", end="\n\n")
    print("Päivä\t\t    Pvm\t\t   Kulutus [kWh]\t Tuotanto [kWh]")
    print("\t\t(pv.kk.vvvv)\tv1\tv2\tv3  \tv1\tv2\tv3")
    print("---------------------------------------------------------------------------")
    print("Maanantai\t", sahkodata[0][0].strftime("%d.%m.%Y"),)
    print("Tiistai\t", )
    print("Keskiviikko\t",)
    print("Torstai\t",)
    print("Perjantai\t",)
    print("Lauantai\t",)
    print("Sunnuntai\t",)

if __name__ == "__main__":
    main()