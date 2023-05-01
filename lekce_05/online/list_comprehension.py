# Chroustání seznamů = List comprehension

# Priklad 1
znamky = [0, 2, 0, 1, 1, 3] # znamkovani programatoru

opravene_znamky = [] # bezne znamkovani (o 1 vetsi)
for znamka in znamky:
    opravene_znamky.append(znamka + 1)
    # opravene_znamky = opravene_znamky + [znamka + 1]
print(opravene_znamky)

# Priklad 2 
kilometry = [2.4, 2.6, 0, 3.5, 1.8]
zaokrouhlene_kilometry = []
for zaznam in kilometry:
    zaokrouhlene_kilometry.append(round(zaznam))
    # zaokrouhlene_kilometry = zaokrouhlene_kilometry + [round(zaznam)]

print(zaokrouhlene_kilometry)

# Priklad 1 - list comprehension
znamky = [0, 2, 0, 1, 1, 3] # znamkovani programatoru
opravene_znamky = [znamka + 1 for znamka in znamky] # modifikace x for x in puvodni seznam
print(opravene_znamky)

# Priklad 2 - list comprehension
kilometry = [2.4, 2.6, 0, 3.5, 1.8]
zaokrouhlene_kilometry = [round(zaznam) for zaznam in kilometry]
print(zaokrouhlene_kilometry)


# místo if znamka < 3:
#     opravene_znamky.append(znamka + 1)
# else:
#     opravene_znamky.append(znamka)

# Znamky - opravime jen znamky, které jsou < 3
znamky = [0, 2, 0, 1, 1, 3] # znamkovani programatoru
opravene_znamky = [znamka + 1 if znamka < 3 else znamka for znamka in znamky] # modifikace x for x in puvodni seznam
print(opravene_znamky)


# Znamky - opravime jen znamky, které jsou < 3
znamky = [0, 2, 0, 1, 1, 3] # znamkovani programatoru

def oprav_znamku(znamka: int) -> int:
    if znamka < 3:
        return znamka + 1
    else:
        return znamka

#opravene_znamky = [oprav_znamku(znamka) for znamka in znamky]
opravene_znamky = [oprav_znamku(x) for x in znamky]
print(opravene_znamky)
print(opravene_znamky)