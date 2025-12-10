# Copyright (c) 2025 Henna Linnala
# License: MIT

from datetime import datetime, date, timedelta
from typing import List

def muunna_tiedot(sahko: list) -> List:
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
    """Muuttaa päivämäärän muotoilun suomalaiseen muotoon (pv.kk.vuosi)"""
    suom_pvm = f"{aika.day}.{aika.month}.{aika.year}"
    return suom_pvm

def paivittainen_data(paiva: date, sahkodata: list) -> list:
    """"Laskee kulutuksen ja tuotannon tiedot. 
    Palauttaa ne listana.
    Laskee suureen muutoksen watti tunneista(Wh) kilowatteihin tunteihin(kWh)
    Muuttaa lasketut kWh arvot muodosta '0.00', suomalaiseen '0,00'-muotoon"""
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
    kulutus[0] = f"{kulutus[0]:.2f}".replace(".", ",")
    kulutus[1] = f"{kulutus[1]:.2f}".replace(".", ",")
    kulutus[2] = f"{kulutus[2]:.2f}".replace(".", ",")
    tuotanto[0] = f"{tuotanto[0]:.2f}".replace(".", ",")
    tuotanto[1] = f"{tuotanto[1]:.2f}".replace(".", ",")
    tuotanto[2] = f"{tuotanto[2]:.2f}".replace(".", ",")

    return f"{kulutus[0]}\t{kulutus[1]}\t{kulutus[2]}\t{tuotanto[0]}\t{tuotanto[1]}\t{tuotanto[2]}" 
    #Tämän returnin kanssa sai taistella, jottei arvot tule ['0,00']['0,00']['0,00]..etc.-muodossa tai muussa tyhmässä muodossa

def viikkoraportti(viikkonumero: int, aloitus_pvm: datetime.date, sahkodata: list) -> str:
    """ Laskee viikkoraportin annettuihin viikonpäiviin ja muodostaa
    Parametrit:
    viikkonumero (int): Raportoivan viikon numero
    aloituspv (datetime.date): Viikon ensimmäinen päivämäärä
    tietokanta (list): Kulutus- ja tuotantotiedot + päivämäärät
    Raportti palautuu tekstinä (str)"""

    viikonpaivat = ["Maanantai", "Tiistai\t", "Keskiviikko", "Torstai\t", "Perjantai", "Lauantai", "Sunnuntai"]

    viikon_raportti = f"\nViikon {viikkonumero} sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n\n"
    viikon_raportti += "Viikonäivä\tPäivämäärä\tKulutus [kWh]\t\tTuotanto [kWh]\n"
    viikon_raportti += "\t\t\t\t\t\tv1\t\tv2\t\tv3\t\tv1\t\tv2\t\tv3\n"
    viikon_raportti += "----------------------------------------------------------------------------\n"
    for i, paiva in enumerate(viikonpaivat):
        paiva = aloitus_pvm + timedelta(days=i)
        if viikonpaivat[i] == viikonpaivat[6]: #Woo sain tämän toimimaan, ihan tyyli syistä...halusin sunnuntain ja "---" väliin isomman välin
            viikon_raportti += f"{viikonpaivat[i]}\t{suomalainen_pvm(paiva)}\t{paivittainen_data(paiva, sahkodata)}\n\n"
        else:
            viikon_raportti += f"{viikonpaivat[i]}\t{suomalainen_pvm(paiva)}\t{paivittainen_data(paiva, sahkodata)}\n"

    viikon_raportti += "----------------------------------------------------------------------------\n"
    return viikon_raportti


def main():
    """ Ohjelman pääfunktio (main) lukee datan annetuista tiedostoista. Luo raportit. Kirjoittaa ja tallentaa tiedot txt-tiedostoon."""
    Viikko41 = sahkonkulutus_ja_tuotanto("viikko41.csv")
    Viikko42 = sahkonkulutus_ja_tuotanto("viikko42.csv")
    Viikko43 = sahkonkulutus_ja_tuotanto("viikko43.csv")

    raportti_viikko_41 = viikkoraportti(41, date(2025, 10, 6), Viikko41)
    raportti_viikko_42 = viikkoraportti(42, date(2025, 10, 13), Viikko42)
    raportti_viikko_43 = viikkoraportti(43, date(2025, 10, 20), Viikko43)

    with open("yhteenveto.txt", "w", encoding="utf-8") as f:
        f.write(raportti_viikko_41)
        f.write(raportti_viikko_42)
        f.write(raportti_viikko_43)

    print("Raportti valmis!")

if __name__ == "__main__":
    main()