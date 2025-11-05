from datetime import datetime
"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin. Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19.95 €
Kokonaishinta: 39.9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""

def main():
    # Määritellään tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"

    # Avataan tiedosto ja luetaan sisältö
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()

    # Tulostetaan varaus konsoliin
    print(varaus)

    # Kokeile näitä
    #print(varaus.split('|'))
    #varausId = varaus.split('|')[0]
    #print(varausId)
    #print(type(varausId))
    varausnumero = int(varaus.split('|')[0])
    print("Varausnumero:", varausnumero)
    varaajannimi = varaus.split('|')[1]
    print("Varaaja:", varaajannimi)
    paivamaara = datetime.strptime(varaus.split('|')[2], ("%Y-%m-%d")).date()
    print("Päivämäärä:",paivamaara.strftime("%d.%m.%Y"))
    aloitusaika = datetime.strptime(varaus.split('|')[3], "%H:%M").time()
    print("Aloitusaika:", aloitusaika.strftime("%H.%M"))
    tuntimaara = int(varaus.split('|')[4])
    print("Tuntimäärä:", tuntimaara)
    tuntihinta = float(varaus.split('|')[5])
    print("Tuntihinta:", tuntihinta, "€")

    """
    Edellisen olisi pitänyt tulostaa numeron 123, joka
    on oletuksena tekstiä.

    Voit kokeilla myös vaihtaa kohdan [0] esim. seuraavaksi [1]
    ja testata mikä muuttuu
    """

if __name__ == "__main__":
    main()