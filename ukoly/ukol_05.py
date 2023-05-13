# Mějme zadaný následující seznam naměřených teplot. Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.

# teploty = [
#     [2.1, 5.2, 6.1, -0.1],
#     [2.2, 4.8, 5.6, -1.0],
#     [3.3, 6.5, 5.9, 1.2],
#     [2.9, 5.6, 6.0, 0.0],
#     [2.0, 4.6, 5.5, -1.2],
#     [1.0, 3.2, 2.1, -2.0],
#     [0.4, 2.7, 1.3, -2.8]
# ]
# Vytvoř seznam průměrných teplot pro každý den.
# Vytvoř seznam ranních teplot.
# Vytvoř seznam nočních teplot.
# Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

prumerne_teploty = [round(sum(den)/len(den), 2) for den in teploty]
print(prumerne_teploty)

ranni_teploty = [den[0] for den in teploty]
print(ranni_teploty)

nocni_teploty = [den[-1] for den in teploty]
print(nocni_teploty)

dvanactH_teploty = [den[1:4:2] for den in teploty]
print(dvanactH_teploty)

# Nepovinný bonus
# Krom teplot máme k dispozici i informaci o dnu v týdnu:

teploty = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]

# Pomocí dict comprehension vytvoř slovník, který bude mít následující formát, kde klíčem bude den v týdnu, a hodnotou průměrná teplota ten den.
# {den: průměrná teplota}
# 
# Dict comprehension si ukážeme až v 6. lekci, ale princip je velice podobný list comprehension. Tady je příklad využit - vytvoříme nový slovník, který nebude body znázorňovat jako celá čísla, ale jako procenta:
#  
# hodnoceni = {"Marie": 62, "Magdalena": 74, "Monika": 93, "Marek": 80}
# 
# procenta = {zak: f"{body}%" for zak, body in hodnoceni.items()}
# procenta = {zak: str(body) + "%" for zak, body in hodnoceni.items()}
# 
# nebo
# 
# procenta = {zak: f"{hodnoceni[zak]}%" for zak in hodnoceni}
# procenta = {zak: str(hodnoceni[zak]) + "%" for zak in hodnoceni}
# 
# print(procenta)  # {'Marie': '62%', 'Magdalena': '74%', 'Monika': '93%', 'Marek': '80%'}

# prumerne_teploty = [round(sum(den)/len(den), 2) for den in teploty]
# print(prumerne_teploty)