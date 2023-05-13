# class Zamestnanec(): # definici tridy
#     def __init__(self, jmeno, pozice): # konstruktor tridy - specialni metoda
#         self.jmeno = jmeno
#         self.pozice = pozice

#     def __str__(self): # specialni metoda
#         return f"Zamestnanec {self.jmeno} pracuje na pozici {self.pozice}"
    
# class Manazer(Zamestnanec): # Manazer dedí od Zamestnance - Manazer prebira atributy a metody Zamestnance
#     def __init__(self, jmeno, pozice, pocet_podrizenych):
#         #Zamestnanec.__init__(self, jmeno, pozice)
#         super().__init__(jmeno, pozice)
#         self.pocet_podrizenych = pocet_podrizenych

# alena = Manazer(jmeno="Alena", pozice="Sefova vsech ucetni", pocet_podrizenych=3)
# print(alena.jmeno)
# print(alena.pozice)
# print(alena.pocet_podrizenych)
# 7:53
# class Manazer(Zamestnanec): # Manazer dedí od Zamestnance - Manazer prebira atributy a metody Zamestnance
#     def __init__(self, jmeno, pozice, pocet_podrizenych):
#         #Zamestnanec.__init__(self, jmeno, pozice)
#         super().__init__(jmeno, pozice)
#         self.pocet_podrizenych = pocet_podrizenych

#     def __str__(self):
#         return f"{super().__str__()} a má tým o velikosti {self.pocet_podrizenych}"

# alena = Manazer(jmeno="Alena", pozice="Sefova vsech ucetni", pocet_podrizenych=3)
# print(alena)


# Janka Marschalkova
#   8:02 PM
# class Manazer(Zamestnanec): # Manazer dedí od Zamestnance - Manazer prebira atributy a metody Zamestnance
#     def __init__(self, jmeno, pocet_podrizenych):
#         super().__init__(jmeno, pozice="manazer")
#         self.pocet_podrizenych = pocet_podrizenych

#     def __str__(self):
#         return f"{super().__str__()} a má tým o velikosti {self.pocet_podrizenych}"

# alena = Manazer(jmeno="Alena", pocet_podrizenych=3)
# milan = Manazer("Milan Velký", pocet_podrizenych=5)
# print(alena)
# print(milan)


# Janka Marschalkova
#   8:09 PM

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