# Napiš funkci total_price, která vypočte cenu noci v hotelu. Funkce bude mít dva parametry - persons a breakfast. Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč. Funkce vrátí výslednou cenu. Parametr breakfast je nepovinný a výchozí hodnota je False.

# Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. total_price(3), total_price(2, True).

def total_price(persons, breakfast = False):
    """
    popis funkce
    """
    if breakfast:
        price = persons * (850 + 125)
    else:
        price = persons * 850
    return price
# testovani funkce
# print(total_price(1, ))
# print(total_price(3, False))
# print(total_price(3, True))

persons = int(input("Počet osob? "))
breakfast = str(input("Se snídaní? "))
if breakfast == "ano":
    breakfast = True
else:
    breakfast = False
print(f"Cena za ubytování {total_price(persons, breakfast)}")