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

def paivittainen_data(paiva: str, sahkodata: list) -> int:
    """Laskee kulutuksen ja tuotannon tiedot 
    Palauttaa ne listana
    Laskee suureen muutoksen watti tunneista(Wh) kilowatteihin tunteihin(kWh)"""
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
    """"Pääohjelma, jonka tehtävänä on lukea data, laskea yhteenvedot ja tulostaa raportti"""
    sahkodata = sahkonkulutus_ja_tuotanto("viikko42.csv")
    print("\n\tViikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)", end="\n\n")
    print("Päivä\t\t    Pvm\t\t   Kulutus [kWh]\t Tuotanto [kWh]")
    print("\t\t(pv.kk.vvvv) \tv1\tv2\tv3  \tv1\tv2\tv3")
    print("---------------------------------------------------------------------------")
    maanantain_data = paivittainen_data("13.10.2025", sahkodata)
    print("Maanantai\t" + "13.10.2025" +"   ", f"{maanantain_data[0]:.2f}".replace('.', ','), end= "\t")
    print(f"{maanantain_data[1]:.2f}".replace('.', ','), end= "\t")
    print(f"{maanantain_data[2]:.2f}".replace('.', ','), end= "\t")
    print(f"{maanantain_data[3]:.2f}".replace('.', ','), end= "\t")
    print(f"{maanantain_data[4]:.2f}".replace('.', ','), end= "\t")
    print(f"{maanantain_data[5]:.2f}".replace('.', ','))
    tiistain_data = paivittainen_data("14.10.2025", sahkodata)
    print("Tiistai\t\t" + "14.10.2025" +"   ", f"{tiistain_data[0]:.2f}".replace('.', ','), end= "\t")
    print(f"{tiistain_data[1]:.2f}".replace('.', ','), end= "\t")
    print(f"{tiistain_data[2]:.2f}".replace('.', ','), end= "\t")
    print(f"{tiistain_data[3]:.2f}".replace('.', ','), end= "\t")
    print(f"{tiistain_data[4]:.2f}".replace('.', ','), end= "\t")
    print(f"{tiistain_data[5]:.2f}".replace('.', ','))
    keskiviikon_data = paivittainen_data("15.10.2025", sahkodata)
    print("Keskiviikko\t" + "15.10.2025" +"   ", f"{keskiviikon_data[0]:.2f}".replace('.', ','), end= "\t")
    print(f"{keskiviikon_data[1]:.2f}".replace('.', ','), end= "\t")
    print(f"{keskiviikon_data[2]:.2f}".replace('.', ','), end= "\t")
    print(f"{keskiviikon_data[3]:.2f}".replace('.', ','), end= "\t")
    print(f"{keskiviikon_data[4]:.2f}".replace('.', ','), end= "\t")
    print(f"{keskiviikon_data[5]:.2f}".replace('.', ','))
    torstain_data = paivittainen_data("16.10.2025", sahkodata)
    print("Torstai\t\t" + "16.10.2025" +"   ", f"{torstain_data[0]:.2f}".replace('.', ','), end= "\t")
    print(f"{torstain_data[1]:.2f}".replace('.', ','), end= "\t")
    print(f"{torstain_data[2]:.2f}".replace('.', ','), end= "\t")
    print(f"{torstain_data[3]:.2f}".replace('.', ','), end= "\t")
    print(f"{torstain_data[4]:.2f}".replace('.', ','), end= "\t")
    print(f"{torstain_data[5]:.2f}".replace('.', ','))
    perjantain_data = paivittainen_data("17.10.2025", sahkodata)
    print("Perjantai\t" + "17.10.2025" +"   ", f"{perjantain_data[0]:.2f}".replace('.', ','), end= "\t")
    print(f"{perjantain_data[1]:.2f}".replace('.', ','), end= "\t")
    print(f"{perjantain_data[2]:.2f}".replace('.', ','), end= "\t")
    print(f"{perjantain_data[3]:.2f}".replace('.', ','), end= "\t")
    print(f"{perjantain_data[4]:.2f}".replace('.', ','), end= "\t")
    print(f"{perjantain_data[5]:.2f}".replace('.', ','))
    lauantain_data = paivittainen_data("18.10.2025", sahkodata)
    print("Lauantai\t" + "18.10.2025" +"   ", f"{lauantain_data[0]:.2f}".replace('.', ','), end= "\t")
    print(f"{lauantain_data[1]:.2f}".replace('.', ','), end= "\t")
    print(f"{lauantain_data[2]:.2f}".replace('.', ','), end= "\t")
    print(f"{lauantain_data[3]:.2f}".replace('.', ','), end= "\t")
    print(f"{lauantain_data[4]:.2f}".replace('.', ','), end= "\t")
    print(f"{lauantain_data[5]:.2f}".replace('.', ','))
    sunnuntain_data = paivittainen_data("19.10.2025", sahkodata)
    print("Sunnuntai\t" + "19.10.2025" +"   ", f"{sunnuntain_data[0]:.2f}".replace('.', ','), end= "\t")
    print(f"{sunnuntain_data[1]:.2f}".replace('.', ','), end= "\t")
    print(f"{sunnuntain_data[2]:.2f}".replace('.', ','), end= "\t")
    print(f"{sunnuntain_data[3]:.2f}".replace('.', ','), end= "\t")
    print(f"{sunnuntain_data[4]:.2f}".replace('.', ','), end= "\t")
    print(f"{sunnuntain_data[5]:.2f}".replace('.', ','), end ="\n\n")

if __name__ == "__main__":
    main()
