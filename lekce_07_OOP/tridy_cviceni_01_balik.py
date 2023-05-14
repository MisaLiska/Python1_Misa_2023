# Balík
# 
# Uvažuj, že navrhuješ software pro zásilkovou společnost.
# 
# Vytvoř třídu Balik, která bude mít tři atributy - adresa, hmotnost a doruceno. První dva atributy nastav pomocí parametrů funkce __init__. Parametr doruceno nastav na začátku jako False.
# Připoj ke třídě funkci doruc, která změní hodnotu parametru doruceno na True.
# Přidej metodu __str__, která vypíše adresu, hmotnost a informaci o tom, zda byl balík již doručen.
# Zkus si vytvořit nějaké objekty ze třídy Balik a ověř, že vše funguje.

class Balik:
    def __init__(self, adresa, hmotnost):
        self.adresa = adresa
        self.hmotnost = hmotnost
        self.doruceno = False

    def doruc(self):
        self.doruceno = True

    def __str__(self) -> str:
        return f"Balík na adresu {self.adresa} s hmotností {self.hmotnost} byl {'doručen' if self.doruceno else 'nedoručen'}"
    
balicek = Balik("Praha", 10)
print(balicek)

balicek.doruc()
print(balicek)

# verze od Pavly
# from dataclasses import dataclass
# @dataclass
# class Balik:
#     adresa: str
#     hmotnost: int
#     doruceno: bool = False
#     # def __init__(self, adresa, hmotnost):
#     #     self.adresa = adresa
#     #     self.hmotnost = hmotnost
#     #     self.doruceno = False

#     def doruc(self):
#         self.doruceno = True

#     def __str__(self) -> str:
#         return f"Balik s hmotnosti {self.hmotnost} kg, byl {'dorucen' if self.doruceno else 'nedorucen'} na adresu {self.adresa}"
    

# balik1 = Balik('praha 10', 20)
# print(balik1)

# balik1.doruc()
# print(balik1)