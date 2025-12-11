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
            
    return [f"{kulutus[0]:.2f}".replace(".", ","),
        f"{kulutus[1]:.2f}".replace(".", ","),
        f"{kulutus[2]:.2f}".replace(".", ","),
        f"{tuotanto[0]:.2f}".replace(".", ","),
        f"{tuotanto[1]:.2f}".replace(".", ","),
        f"{tuotanto[2]:.2f}".replace(".", ","),]

def viikkoraportti(viikkonumero: int, aloitus_pvm: datetime.date, sahkodata: list) -> str:
    """ Laskee viikkoraportin annettuihin viikonpäiviin
    Parametrit:
    viikkonumero (int): Raportoivan viikon numero
    aloituspv (datetime.date): Viikon ensimmäinen päivämäärä
    tietokanta (list): Kulutus- ja tuotantotiedot + päivämäärät
    Raportti palautuu tekstinä (str)"""

    viikonpaivat = ["Maanantai", "Tiistai\t", "Keskiviikko", "Torstai\t", "Perjantai", "Lauantai", "Sunnuntai"]

    viikon_raportti = f"\n\t\tViikon {viikkonumero} sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n\n"
    viikon_raportti += "Viikonäivä\t\tPäivämäärä\t\t\tKulutus [kWh]\t\t\tTuotanto [kWh]\n"
    viikon_raportti += "\t\t\t    (pv.kk.vvvv) \t v1\t\t v2\t\t v3\t\t v1\t\t v2\t\t v3\n"
    viikon_raportti += "------------------------------------------------------------------------------\n"
    for i, paiva in enumerate(viikonpaivat):
        pvm = aloitus_pvm+timedelta(days=i)
        if viikonpaivat[i] == viikonpaivat[6]: #Woo sain tämän toimimaan...halusin sunnuntain ja "---" väliin isomman välin
            viikon_raportti += paiva + "\t\t"+ (suomalainen_pvm(pvm))+"\t\t" + "\t".join(paivittainen_data(pvm, sahkodata)) + "\n\n"
        else:
            viikon_raportti += paiva + "\t\t"+ (suomalainen_pvm(pvm))+"\t\t" + "\t".join(paivittainen_data(pvm, sahkodata)) + "\n"

    viikon_raportti += "------------------------------------------------------------------------------\n"
    return viikon_raportti

def main():
    """ Ohjelman pääfunktio (main) lukee datan annetuista tiedostoista. Luo raportit. 
    Kirjoittaa ja tallentaa tiedot txt-tiedostoon."""
    viikko41 = sahkonkulutus_ja_tuotanto("viikko41.csv")
    viikko42 = sahkonkulutus_ja_tuotanto("viikko42.csv")
    viikko43 = sahkonkulutus_ja_tuotanto("viikko43.csv")

    raportti_viikko41 = viikkoraportti(41, date(2025, 10, 6), viikko41)
    raportti_viikko42 = viikkoraportti(42, date(2025, 10, 13), viikko42)
    raportti_viikko43 = viikkoraportti(43, date(2025, 10, 20), viikko43)

    with open("yhteenveto.txt", "w", encoding="utf-8") as f:
        f.write(raportti_viikko41)
        f.write(raportti_viikko42)
        f.write(raportti_viikko43)

    print("Raportti valmis!")

if __name__ == "__main__":
    main()