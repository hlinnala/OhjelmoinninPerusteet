# Copyright (c) 2025 Henna Linnala
# License: MIT

"""Kokeillaan olioita"""
from datetime import datetime
from typing import Dict, List

def muunna_varaustiedot(varaus_lista: list[str]) -> Varaus:
    """Muuttaa tietojen tietotyyppiä ja luo niistä olion"""
    return Varaus(
        varaus_id=int(varaus_lista[0]),
        nimi=varaus_lista[1],
        sahkoposti=varaus_lista[2],
        puhelin=varaus_lista[3],
        paiva=datetime.strptime(varaus_lista[4], "%Y-%m-%d").date(),
        aika=datetime.strptime(varaus_lista[5], "%H:%M").time(),
        kesto=int(varaus_lista[6]),
        hinta=float(varaus_lista[7]),
        vahvistettu=(varaus_lista[8].lower() == "true"),
        kohde=varaus_lista[9],
        luotu=datetime.strptime(varaus_lista[10], "%Y-%m-%d %H:%M:%S")    
    )
class Varaus:
    def __init__(self, varaus_id, nimi, sahkoposti, puhelin,
                 paiva, aika, kesto, hinta,
                 vahvistettu, kohde, luotu):
        self.varaus_id = varaus_id
        self.nimi = nimi
        self.sahkoposti = sahkoposti
        self.puhelin = puhelin
        self.paiva = paiva
        self.aika = aika
        self.kesto = kesto
        self.hinta = hinta
        self.vahvistettu = vahvistettu
        self.kohde = kohde
        self.luotu = luotu

def hae_varaukset(varaus_lista: str) -> List[Varaus]:
    """Lukee CSV-tiedoston ja palauttaa rivit"""
    varaukset = []
    varaukset.append(["varaus_id", "nimi", "sähköposti", "puhelin", "paiva", "aika", "kesto", "hinta", "vahvistettu", "kohde", "luotu"])
    with open(varaus_lista, "r", encoding="utf-8") as f:
        for varaus in f:
            varaus = varaus.strip()
            varaustiedot = varaus.split('|')
            varaukset.append(muunna_varaustiedot(varaustiedot))
    return varaukset

def vahvistetut_varaukset(varaukset:List[Varaus]):
    for varaus in varaukset[1:]:
        if varaus.is_confirmed():
            print(f"- {varaus.nimi}, {varaus.kohde}, {varaus.paiva.strftime('%d.%m.%Y')}")
            return self.vahvistettu

    print()

def pitkat_varaukset(varaukset: list):
    for varaus in varaukset[1:]:
        if(varaus["kesto"] >= 3):
            print(f"- {varaus["nimi"]}, {varaus["paiva"].strftime('%d.%m.%Y')} klo {varaus["aika"].strftime('%H.%M')}, kesto {varaus["kesto"]} h, {varaus["kohde"]}")

    print()

def varausten_vahvistusstatus(varaukset: list):
    for varaus in varaukset[1:]:
        if(varaus["vahvistettu"]):
            print(f"{varaus["nimi"]} → Vahvistettu")
        else:
            print(f"{varaus["nimi"]} → EI vahvistettu")

    print()

def varausten_lkm(varaukset: list):
    vahvistetut_varaukset = 0
    ei_vahvistetut_varaukset = 0
    for varaus in varaukset[1:]:
        if(varaus["vahvistettu"]):
            vahvistetut_varaukset += 1
        else:
            ei_vahvistetut_varaukset += 1

    print(f"- Vahvistettuja varauksia: {vahvistetut_varaukset} kpl")
    print(f"- Ei-vahvistettuja varauksia: {ei_vahvistetut_varaukset} kpl")
    print()

def varausten_kokonaistulot(varaukset: list):
    varausten_tulot = 0
    for varaus in varaukset[1:]:
        if(varaus["vahvistettu"]):
            varausten_tulot += varaus["kesto"]*varaus["hinta"]

    print("Vahvistettujen varausten kokonaistulot:", f"{varausten_tulot:.2f}".replace('.', ','), "€")
    print()

def main():
    varaukset = hae_varaukset("varaukset.txt")
    print("1) Vahvistetut varaukset")
    vahvistetut_varaukset(varaukset)
    print("2) Pitkät varaukset (≥ 3 h)")
    pitkat_varaukset(varaukset)
    print("3) Varausten vahvistusstatus")
    varausten_vahvistusstatus(varaukset)
    print("4) Yhteenveto vahvistuksista")
    varausten_lkm(varaukset)
    print("5) Vahvistettujen varausten kokonaistulot")
    varausten_kokonaistulot(varaukset)

if __name__ == "__main__":
    main()