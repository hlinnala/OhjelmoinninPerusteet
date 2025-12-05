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

def sahkonkulutus_ja_tuotanto(data: str) -> list:
    """Lukee CSV-tiedoston ja palauttaa rivit"""
    """Next(f) poistaa esittelytiedon"""
    sahkodata = []
    with open(data, "r", encoding="utf-8") as f:
        next(f) 
        for sahko in f:
            sahko = sahko.strip()
            sahkon_tiedot = sahko.split(';')
            sahkodata.append(muunna_tiedot(sahkon_tiedot))
    return sahkodata


from datetime import date

def paivittainen_data(paiva: str, sahkodata: list) -> int:
    vuorokausi = int(paiva.split(".")[0])
    kuukausi = int(paiva.split(".")[1])
    vuosi = int(paiva.split(".")[2])
    tiedot = []
    kulutus = [0, 0, 0]
    tuotanto = [0, 0, 0]
    for data in sahkodata:
        if data[0].date() == date(vuosi, kuukausi, vuorokausi):
            kulutus[0] += data[1] 
            kulutus[1] += data[2] 
            kulutus[2] += data[3] 
            tuotanto[0] += data[4] 
            tuotanto[1] += data [5]
            tuotanto[2] += data[6] 

    tiedot.append(kulutus[0]/1000)
    tiedot.append(kulutus[1]/1000)
    tiedot.append(kulutus[2]/1000)
    tiedot.append(tuotanto[0]/1000)
    tiedot.append(tuotanto[1]/1000)
    tiedot.append(tuotanto[2]/1000)
    return tiedot


def main():
    """"Pääohjelma, jonka tehtävänä on lukea data, laskea yhteenvedot ja tulostaa raportti ellen jotenkin muuta koko hommaa"""
    sahkodata = sahkonkulutus_ja_tuotanto("viikko42.csv")
    print("\n\tViikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)", end="\n\n")
    print("Päivä\t\t    Pvm\t\t   Kulutus [kWh]\t Tuotanto [kWh]")
    print("\t\t(pv.kk.vvvv) \tv1\tv2\tv3  \tv1\tv2\tv3")
    print("---------------------------------------------------------------------------")
    maanantain_data = paivittainen_data("13.10.2025", sahkodata)
    print("Maanantai\t" + "13.10.2025\t",f"{maanantain_data[0]:.2f}".replace('.', ','), end= "\t")
    print(f"{maanantain_data[1]:.2f}".replace('.', ','), end= "\t")
    print(f"{maanantain_data[2]:.2f}".replace('.', ','), end= "\t")
    print(f"{maanantain_data[3]:.2f}".replace('.', ','), end= "\t")
    print(f"{maanantain_data[4]:.2f}".replace('.', ','), end= "\t")
    print(f"{maanantain_data[5]:.2f}".replace('.', ','))


if __name__ == "__main__":
    main()
