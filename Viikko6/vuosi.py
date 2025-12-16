# Copyright (c) 2025 Henna Linnala
# License: MIT
# tsiisus mikä määrä dataa

from datetime import datetime, date

def muunna_tiedot(sahko: list) -> list:
    """Muuttaa tietojen tietotyyppiä"""
    return [datetime.fromisoformat(sahko[0]),
        float(sahko[1].replace(",", ".")),
        float(sahko[2].replace(",", ".")),
        float(sahko[3].replace(",", ".")),]

def vuosidata(data: str) -> list:
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
    """Kirjoittaa annetun sisällön .txt-tiedostoon
    Parametrit:
     raportti (str): raporttiteksti"""
    with open("raportti.txt", "w", encoding="utf-8") as f:
        f.write(raportti)

def paivaraportti(alkupaiva: datetime.date, loppupaiva: datetime.date, sahkodata: list) -> str:
    """Muodostaa yhteenvedon halutulta aikaväliltä
    Parametrit: 
        alkupaiva(str): aikavälin aloituspaiva
        loppupaiva(str): aikavälin loppupaiva
        sahkodata(list): sisältää kaikki tiedot
    Palauttaa luodun raportin"""

    alkupv = int(alkupaiva.split('.')[0])
    alkukk = int(alkupaiva.split('.')[1])
    alkuvv = int(alkupaiva.split('.')[2])
    alku = date(alkuvv, alkukk, alkupv)
    loppupv = int(loppupaiva.split('.')[0])
    loppukk = int(loppupaiva.split('.')[1])
    loppuvv = int(loppupaiva.split('.')[2])
    loppu = date(loppuvv, loppukk, loppupv)
    kulutus = 0
    tuotanto = 0
    lampotila = 0
    lukumaara = 0
    for sahko in sahkodata:
        if alku <= sahko[0].date() <= loppu:
            kulutus += sahko[1]
            tuotanto += sahko[2]
            lampotila += sahko[3]
            lukumaara += 1

    raportti = "---------------------------------------------------------\n\n"
    raportti += f"\tRaportti aikaväliltä {alkupaiva}-{loppupaiva}\n\n"
    raportti += f"\tKokonaiskulutus: {kulutus:.2f} kWh\n".replace(".",",")
    raportti += f"\tKokonaistuotanto: {tuotanto:.2f} kWh\n".replace(".",",")
    raportti += f"\tKeskilämpötila: {lampotila/lukumaara:.2f} °C\n\n".replace(".",",")
    raportti += "---------------------------------------------------------\n\n"
    return raportti


def kuukausiraportti(kuukausi: str, sahkodata: list) -> list[str]:
    """Muodostaa kuukausikohtaisen yhteenvedon valitulle kuukaudelle.
    Parametrit: 
        kuukausi (str): pyydetty kuukausi
        sahkodata (list): sisältää kaikki tiedot
    Palauttaa luodun raportin"""
    kk = int(kuukausi)
    kuukaudet = ["Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kesäkuu", "Heinäkuu", "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu"]
    kulutus = 0
    tuotanto = 0
    lampotila = 0
    lukumaara = 0
    for sahko in sahkodata:
        if sahko[0].date().month == kk:
            kulutus += sahko[1]
            tuotanto += sahko[2]
            lampotila += sahko[3]
            lukumaara += 1

    raportti = "---------------------------------------------------------\n\n"
    raportti += f"\t\tRaportti kuukaudelta: {kuukaudet[kk-1]}\n\n"
    raportti += f"\tKokonaiskulutus: {kulutus:.2f} kWh\n".replace(".",",")
    raportti += f"\tKokonaistuotanto: {tuotanto:.2f} kWh\n".replace(".",",")
    raportti += f"\tKeskilämpötila: {lampotila/lukumaara:.2f} °C\n\n".replace(".",",")
    raportti += "--------------------------------------------------------\n\n"
    return raportti

def vuosiraportti(sahkodata: list) -> list[str]:
    """Muodostaa koko vuoden yhteenvedon.
    Parametrit:
        sahkodata (list): sisältää kaikki tiedot
    Palauttaa luodun raportin"""
    kulutus = 0
    tuotanto = 0
    lampotila = 0
    lukumaara = 0
    for paiva in sahkodata:
            kulutus += paiva[1]
            tuotanto += paiva[2]
            lampotila += paiva[3]
            lukumaara += 1

    raportti = "--------------------------------------------------------\n\n"
    raportti += f"\t\tRaportti koko vuodelta 2025\n\r"
    raportti += f"\tVuoden 2025 kokonaiskulutus: {kulutus:.2f} kWh\n".replace(".",",")
    raportti += f"\tVuoden 2025 kokonaistuotanto: {tuotanto:.2f} kWh\n".replace(".",",")
    raportti += f"\tVuoden 2025 keskilämpötila: {lampotila/lukumaara:.2f} °C\n\n".replace(".",",")
    raportti += "--------------------------------------------------------\n\n"
    return raportti

def main():
    "Ohjelman pääfunktio "
    kulutus_tuotanto = vuosidata("2025.csv")

    while True:
        print("\nValitse raporttityyppi:")
        print("1) Päiväkohtainen yhteenveto valitulta aikaväliltä")
        print("2) Kuukausikohtainen yhteenveto yhdelle kuukaudelle")
        print("3) Vuoden 2025 kokonaisyhteenveto")
        print("4) Lopeta ohjelma")
        ensimmainen_valinta = int(input("Anna valinta (numero 1-4): "))
        if ensimmainen_valinta == 1:
            alkupaiva = input("Anna alkupäivä (pv.kk.vvvv): ")
            loppupaiva = input("Anna loppupäivä (pv.kk.vvvv): ")
            raportti = paivaraportti(alkupaiva, loppupaiva, kulutus_tuotanto)
            print(raportti)
        elif ensimmainen_valinta == 2:
            kuukausi = input("Anna kuukauden numero (1–12): ")
            raportti = kuukausiraportti(kuukausi, kulutus_tuotanto)
            print(raportti)
        elif ensimmainen_valinta == 3:
            print("\nVuosiraportti tulostuu...")
            raportti = vuosiraportti(kulutus_tuotanto)
            print(raportti)
        elif ensimmainen_valinta == 4:
            print("Lopetetaan ohjelma...")
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
            raportti_tiedostoon(raportti)
            print("\nRaportti valmis! Löydät sen nimellä raportti.txt.")
        elif toinen_valinta == 2:
            continue
        elif toinen_valinta == 3:
            print("Lopetetaan ohjelma...")
            break
        else:
            continue

        print("---------------------------------------------------------")

if __name__ == "__main__":
    main()