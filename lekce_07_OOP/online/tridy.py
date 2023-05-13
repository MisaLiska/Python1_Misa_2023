# class Zamestnanec: # definici tridy
#     jmeno = ""
#     pozice = ""

# frantisek = Zamestnanec() # objekt
# 6:16
# frantisek = Zamestnanec() # objekt
# frantisek.jmeno = "Frantisek Novak"
# frantisek.pozice = "ucetni"

# print(frantisek.pozice)


# Janka Marschalkova
#   6:34 PM
# class Zamestnanec: # definici tridy
#     def __init__(self, jmeno, pozice): # konstruktor tridy - specialni metoda
#         self.jmeno = jmeno
#         self.pozice = pozice

#     def info(self): # metoda tridy 
#         return f"Zamestnanec {self.jmeno} pracuje na pozici {self.pozice}"

# frantisek = Zamestnanec("Frantisek Novotny", "ucetni") # objekt - pri vytvareni se nam zavola __init__
# alena = Zamestnanec("Alena Drobna", "sefova")

# print(frantisek.info())
# New


# Janka Marschalkova
#   6:39 PM
class Zamestnanec: # definici tridy
    def __init__(self, jmeno, pozice): # konstruktor tridy - specialni metoda
        self.jmeno = jmeno
        self.pozice = pozice
        self.pocet_dni_dovolene = 25

    def __str__(self): # specialni metoda
        return f"Zamestnanec {self.jmeno} pracuje na pozici {self.pozice}"

    def info(self): # metoda tridy 
        return f"Zamestnanec {self.jmeno} pracuje na pozici {self.pozice}"
    
    def cerpani_dovolene(self, days):
        if self.pocet_dni_dovolene >= days:
            self.pocet_dni_dovolene -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.pocet_dni_dovolene} dní."

frantisek = Zamestnanec("Frantisek Novotny", "ucetni") # objekt - pri vytvareni se nam zavola __init__
alena = Zamestnanec("Alena Drobna", "sefova")

print(frantisek.cerpani_dovolene(5))
print(frantisek.pocet_dni_dovolene)
print(frantisek.cerpani_dovolene(15))
print(frantisek.pocet_dni_dovolene)
print(frantisek.cerpani_dovolene(15))
print(alena.pocet_dni_dovolene)