# Částečný úvazek
#
# Naše firma se rozhodla zaměstnávat i pracovníky na částečné úvazky, pro které bude vytvořena zvláštní třída. Vytvoř novou třídu Brigadnik, která bude dědit od třídy Zamestnanec a bude mít navíc atribut uvazek, který reprezentuje velikost úvazku oproti plnému. Přidej informaci o úvazku k výpisu informací do funkce __str__.

class Zamestnanec(): # definici tridy
    def __init__(self, jmeno, pozice): # konstruktor tridy - specialni metoda
        self.jmeno = jmeno
        self.pozice = pozice

    def __str__(self): # specialni metoda
        return f"Zamestnanec {self.jmeno} pracuje na pozici {self.pozice}"
    


class Manazer(Zamestnanec): # Manazer dedí od Zamestnance - Manazer prebira atributy a metody Zamestnance
    def __init__(self, jmeno, pocet_podrizenych = 3):
        super().__init__(jmeno, pozice="manazer")
        self.podrizeni = []

    def __str__(self):
        return f"{super().__str__()} a má tým o velikosti {self.pocet_podrizenych}"
    
    def pridej_podrizeneho(self, novy_podrizeny):
        self.podrizeni.append(novy_podrizeny)
    
    def vypis_podrizene(self):
        podrizeni = ""
        for person in self.podrizeni:
            podrizeni += person.jmeno + ", "
        return podrizeni
    
frantisek = Zamestnanec("Frantisek", "ucetni")
alena = Manazer(jmeno="Alena", pocet_podrizenych=3)
alena.pridej_podrizeneho(frantisek)
print(alena.vypis_podrizene())