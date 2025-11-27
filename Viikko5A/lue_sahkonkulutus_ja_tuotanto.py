# Copyright (c) 2025 Henna Linnala
# License: MIT
from datetime import datetime
from typing import List, Dict



#def esimerkki(arvo: int) -> float:
#    """Muuntaa kokonaisluvun liukuluvuksi ja palauttaa arvon kerrottuna kymmenellä."""

#def hae_paiva(sahko: list[str]) -> datetime:
#    paivamaara = datetime.strptime(sahko[0], "%Y-%m-%d").date()
#    suomalainenpvm = paivamaara.strftime("%d.%m.%Y")
#    return suomalainenpvm
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
    #sahkodata.append(["aika", "kulutus_1", "kulutus_2", "kulutus_3", "tuotanto_1", "tuotanto_2", "tuotanto_3"])
    with open(data, "r", encoding="utf-8") as f:
        next(f) #Ottaa sarakeiden esittelytiteo pois
        for sahko in f:
            sahko = sahko.strip()
            sahkon_tiedot = sahko.split(';')
            sahkodata.append(muunna_tiedot(sahkon_tiedot))
    return sahkodata

#sahkonkulutus_ja_tuotanto = "viikko42.csv"
#with open(sahkonkulutus_ja_tuotanto, "r", encoding="utf-8") as f:
#    sahko = f.read().strip()
#    sahko = sahko.split(';')

#print(sahko)
#print(sahko[0])

def main():
    sahkodata = sahkonkulutus_ja_tuotanto("viikko42.csv")
    """Ohjelman pääfunktio: lukee datan, laskee yhteenvedot ja tulostaa raportin."""
    print("Viikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)")
    #print(sahkodata[0][0])
    print("Päivä           Pvm            Kulutus [kWh]                 Tuotanto [kWh]")
    print("           (pv.kk.vvvv)     v1      v2      v3            v1     v2     v3")
    print("---------------------------------------------------------------------------")

if __name__ == "__main__":
    main()