# Seznamy řetězců

# Mějme zadaný následující seznam

# jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']
# Vytvořte seznam, který obsahuje

# počty písmen ve všech jménech,
# všechna jména napsaná velkými písmeny,
# všechna jména plus písmeno 'a' na konci (stanou se z nich tedy ženská jména),
# všechna jména převedená na malá písmena s koncovkou '@email.cz'.

jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']

pocty_pismen = [len(jmeno) for jmeno in jmena]
print(pocty_pismen)

vsechna_velka = [jmeno.upper() for jmeno in jmena]
print(vsechna_velka)