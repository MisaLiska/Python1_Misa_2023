# Seznamy čísel

# Mějme zadaný následující seznam

# cisla = [1.12, 4.51, 2.64, 13.1, 0.1]
# Vytvořte seznam, který obsahuje

# každé z čísel ze seznamu cisla vynásobené dvěma,
# každé z čísel ze seznamu cisla s opačným znaménkem,
# každé z čísel ze seznamu cisla umocněné na druhou,
# každé z čísel ze seznamu cisla jako řetězec.

cisla = [1.12, 4.51, 2.64, 13.1, 0.1]
vynasobena_cisla = [cislo * 2 for cislo in cisla]
opacna_znamenka = [cislo * -1 for cislo in cisla]
druha_mocnina_cisla = [cislo * cislo for cislo in cisla]
retezec_cisla = [str(cislo) for cislo in cisla]
print(vynasobena_cisla)
print(opacna_znamenka)
print(druha_mocnina_cisla)
print(retezec_cisla)
