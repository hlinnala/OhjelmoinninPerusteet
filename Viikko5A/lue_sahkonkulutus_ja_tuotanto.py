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

def paivittainen_data(paiva: date, sahkodata: list) -> list:
    """Laskee kulutuksen ja tuotannon tiedot 
    Palauttaa ne listana
    Laskee suureen muutoksen watti tunneista(Wh) kilowatteihin tunteihin(kWh)"""
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

def suomalainen_pvm(paiva: date):
    """Muuttaa päivämäärän muotoilun suomalaiseen muotoon (pv.kk.vuosi)"""
    suom_pvm= f"{paiva.day}.{paiva.month}.{paiva.year}"
    return suom_pvm
       
def main():
    """"Pääohjelma, jonka tehtävänä on lukea data, laskea yhteenvedot ja tulostaa raportti"""
    sahkodata = sahkonkulutus_ja_tuotanto("viikko42.csv")
    print("\n\tViikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)", end="\n\n")
    print("Päivä\t\t    Pvm\t\t   Kulutus [kWh]\t Tuotanto [kWh]")
    print("\t\t(pv.kk.vvvv) \tv1\tv2\tv3  \tv1\tv2\tv3")
    print("---------------------------------------------------------------------------")
    print("Maanantai\t" + (suomalainen_pvm(date(2025, 10, 13))) + "\t" + "\t".join(paivittainen_data(date(2025, 10, 13), sahkodata)))
    print("Tiistai\t\t" + (suomalainen_pvm(date(2025, 10, 14))) + "\t"+ "\t".join(paivittainen_data(date(2025, 10, 14), sahkodata)))
    print("Keskiviikko\t" + (suomalainen_pvm(date(2025, 10, 15))) + "\t"+ "\t".join(paivittainen_data(date(2025, 10, 15), sahkodata)))
    print("Torstai\t\t" + (suomalainen_pvm(date(2025, 10, 16))) + "\t"+ "\t".join(paivittainen_data(date(2025, 10, 16), sahkodata)))
    print("Perjantai\t" + (suomalainen_pvm(date(2025, 10, 17))) + "\t"+ "\t".join(paivittainen_data(date(2025, 10, 17), sahkodata)))
    print("Lauantai\t" + (suomalainen_pvm(date(2025, 10, 18))) + "\t"+ "\t".join(paivittainen_data(date(2025, 10, 18), sahkodata)))
    print("Sunnuntai\t" + (suomalainen_pvm(date(2025, 10, 19))) + "\t"+ "\t".join(paivittainen_data(date(2025, 10, 19), sahkodata)), end="\n\n")

if __name__ == "__main__":
    main()