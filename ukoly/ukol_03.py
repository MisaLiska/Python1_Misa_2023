# ukol-03
# V tomto úkolu využiješ znalosti z kapitoly Slovníky a cykly

# Zadání
# Soubor body.json je JSON, který obsahuje informace o získaných bodech z písemky.

# Soubor si ulož a načti do slovníku.

# Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). Vytvoř nový slovník. Jeho klíče budou opět jména žáků, a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň než 60 bodů. Pokud má méně než 60, hodnota bude "Fail".

# Výsledný slovník ulož jako JSON do souboru prospech.json.

# Nepovinný bonus
# Krom souboru s body si ulož a načti do druhého slovníku ještě soubor bonusy.json. Obsahuje bonusové body získané během semestru. Pozor, bonusové body získali jen někteří žáci.

# Tvým úkolem je žákům přiřadit známky na základě součtu bodů z písemky a bonusových bodů. Bodová rozhraní (vztahují se na součet) najdeš zde:

# 1: 90 a více
# 2: 70-89
# 3: 50-69
# 4: 30-49
# 5: 29 a méně
# Výsledný slovník ulož jako JSON do souboru znamky.json.

import json

with open('ukoly/body.json', encoding='utf-8') as Inputdata:
    body = json.load(Inputdata)
# print(body)
prospech = {}
for zak, vysledek in body.items():
    # print(f"{zak}, {vysledek}")
    if vysledek >= 60:
        prospech[zak] = "pass"
    else:
        prospech[zak] = "fail"
# print(prospech)

with open('ukoly/prospech.json', "w", encoding='utf-8') as OutputData: #formatovani vystupu, co člověk to řádek a s diakritikou tak jako jsou vstupní data, nefunguje. Jak to vyřešit?
    json.dump(prospech, OutputData)

# BONUS

with open('ukoly/bonusy.json', encoding='utf-8') as Inputdata:
    bonusy = json.load(Inputdata)
# print(bonusy)
znamky = {}
for zak, vysledek in body.items():
    znamky[zak] = vysledek
    for zak2, bonus in bonusy.items():
        if zak == zak2:
            znamky[zak] = vysledek + bonus

with open('ukoly/body_celkem.json', "w", encoding='utf-8') as OutputData: #formatovani vystupu, co člověk to řádek a s diakritikou tak jako jsou vstupní data, nefunguje. Jak to vyřešit?
    json.dump(znamky, OutputData)

for zak, vysledek in znamky.items():
    if vysledek >= 90:
        znamky[zak] = 1
    elif vysledek >= 70:
        znamky[zak] = 2
    elif vysledek >= 50:
        znamky[zak] = 3
    elif vysledek >= 30:
        znamky[zak] = 4
    else:
        znamky[zak] = 5
    
with open('ukoly/znamky.json', "w", encoding='utf-8') as OutputData: #formatovani vystupu, co člověk to řádek a s diakritikou tak jako jsou vstupní data, nefunguje. Jak to vyřešit?
    json.dump(znamky, OutputData)
