KURZ = 28
def eur_to_czk(pocet_eur):
    """
    Funkce na prevod eur do korun.
    Bere jeden parametr - pocet eur. Kurz fixni 25 kc za 1 euro.
    Vrati kolik stoji eura v korunach.
    """
    kurz = 25 # lokalni promenna - neni videt mimo telo funkce
    pocet_czk = pocet_eur * KURZ
    return pocet_czk

eura_uzivatel = int(input("Kolik si prejete smenit euro?"))
print(eur_to_czk(eura_uzivatel))

print(KURZ)

print(eur_to_czk(pocet_eur=eura_uzivatel, kurz=28)) # v pořadí
print(eur_to_czk(kurz=28, pocet_eur=eura_uzivatel)) # při přehození pořadí důležité název=....


print(eur_to_czk(pocet_eur=eura_uzivatel, 28)) # Bacha, nefunguje
print(eur_to_czk(eura_uzivatel, kurz=28, .... = ..., ... = ....)) # OK