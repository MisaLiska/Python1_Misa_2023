a = 2
b = 3

print(a+b)

def secti(l, k): # parametry
    return l + k
    #print(l+k)

secti(8, 5) # argumenty

vysledek = secti(8, 5)
print(f'Vysledek je : {vysledek}')

# Ke kazdemu cislu v seznamu pricti 1 pomoci funkce secti
seznam_cisel = [2, 5, 9, 8]

# Vysledek jen vypiseme
for cislo in seznam_cisel:
    print(secti(cislo, 1))

# Vysledek ulozime do noveho seznamu
soucty = []
for cislo in seznam_cisel:
    soucty.append(secti(cislo, 1))

# Přepíšeme původní seznam_cisel na novy, kde k cislum byla prictena 1 pomocí funkce secti
seznam_cisel = soucty

#funkce bez kódu, se záměrem nakódit později a jen si nyní vyhradit místo v kódu
def code_me_later(a, b):
    pass
