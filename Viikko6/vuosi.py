# Copyright (c) 2025 Henna Linnala
# License: MIT
# #tsiisus mikä määrä dataa

from datetime import datetime, date
from typing import List, Dict

def muunna_tiedot(sahko: list) -> list:
    """Muuttaa tietojen tietotyyppiä"""
    return [datetime.fromisoformat(sahko[0]),
        float(sahko[1].replace(",", ".")),
        float(sahko[2].replace(",", ".")),
        float(sahko[3].replace(",", ".")),]

def sahkonkulutus_ja_tuotanto(data: str) -> List:
    """Lukee CSV-tiedoston ja palauttaa rivit
    Next(f) poistaa esittelytiedon"""
    sahkodata = []
    with open(data, "r", encoding="utf-8") as f:
        next(f) 
        for sahko in f:
            sahko = sahko.split(';')
            sahkodata.append(muunna_tiedot(sahko))
    return sahkodata
def raportti_tiedostoon(raportti: str):
    """
    Kirjoittaa annetun sisällön tiedostoon

    Parametrit:
     raportti (str): raporttiteksti
    """
    with open("raportti.txt", "w", encoding="utf-8") as f:
        f.write(raportti)

def raportti_aikavali(alkupaiva: datetime.date, loppupaiva: datetime.date, tietokanta: list) -> str:
    return True


def main():
    "Ohjelman pääfunktio "
    # Luetaan data tiedostosta
    kulutus_tuotanto = sahkonkulutus_ja_tuotanto("2025.csv")
    #print(len(kulutusTuotanto2025))

    while True:
        print("Valitse raporttityyppi:")
        print("1) Päiväkohtainen yhteenveto aikaväliltä")
        print("2) Kuukausikohtainen yhteenveto yhdelle kuukaudelle")
        print("3) Vuoden 2025 kokonaisyhteenveto")
        print("4) Lopeta ohjelma")
        ensimmainen_valinta = int(input("Anna valinta (numero 1-4): "))
        if ensimmainen_valinta == 1:
            alkupaiva = input("Anna alkupäivä (pv.kk.vvvv): ")
            loppupaiva = input("Anna loppupäivä (pv.kk.vvvv): ")
            print(kulutus_tuotanto[0])
        elif ensimmainen_valinta == 2:
            kuukausi = input("Anna kuukauden numero (1–12): ")
            print(kulutus_tuotanto[1])
        elif ensimmainen_valinta == 3:
            print("vuosiraportti tulostuu...")
        elif ensimmainen_valinta == 4:
            print("Lopetaan ohjelma...")
            break
        else:
            continue

        print("---------------------------------------------------------")
        print("Mitä haluat tehdä seuraavaksi?")
        print("1) Kirjoita raportti tiedostoon raportti.txt")
        print("2) Luo uusi raportti")
        print("3) Lopeta")
        toinen_valinta = int(input("Anna valinta (numero 1-3): "))
        if toinen_valinta == 1:
            raportti_tiedostoon(str(kulutus_tuotanto[0][1]))
        elif toinen_valinta == 2:
            continue
        elif toinen_valinta == 3:
            print("Lopetaan ohjelma...")
            break
        else:
            continue

        print("---------------------------------------------------------")

    #print("Valitsit ", ensimmainen_valinta)


if __name__ == "__main__":
    main()