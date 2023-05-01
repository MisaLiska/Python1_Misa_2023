# def eur_to_czk(pocet_eur, kurz=25):
def eur_to_czk(pocet_eur: int, kurz: int=25) -> int:
    """
    Funkce na prevod eur do korun.
    Bere dva parametry - pocet eur a kurz.
    Vrati kolik stoji eura v korunach.
    """
    pocet_czk = pocet_eur * kurz
    return pocet_czk

eura_uzivatel = input("Kolik si prejete smenit euro?")
print(eur_to_czk(eura_uzivatel))