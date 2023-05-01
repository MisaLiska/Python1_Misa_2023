import random
# cyklus pomocí číselné řady
""" jmena = ["Anna", "Adela", "Alena", "Adam"]

for jmeno in jmena:
    print(jmeno)
 """

pocet_hracu = 4
hod_1 = random.randint(1, 6)
hod_2 = random.randint(1, 6)
hod_3 = random.randint(1, 6)
hod_4 = random.randint(1, 6)

#print(hod_1, hod_2, hod_3, hod_4)

#print(list(range(pocet_hracu)))

#Chceme tolikrat "hodit kostkou" kolik mame hracu
for hrac in range(pocet_hracu): # Opakuj tolikrat, kolik zadame parametr funkci range (zde pocet_hracu)
    print(random.randint(1,6))

# zbytecne bychom museli vypisovat, velke cislo by bylo narocne
for hrac in [0, 1, 2, 3, 4, 5]:
    print(random.randint(1,6))

# Nepojmenovana promenna podtrzitko "_"
for _ in range(pocet_hracu): 
    print(f'Hrac hodil {random.randint(1,6)}')

jmena = ["Anna", "Adela", "Alena", "Adam"]
for hrac in range(pocet_hracu): # Opakuj tolikrat, kolik zadame parametr funkci range (zde pocet_hracu)
    print(f'Hrac {jmena[hrac]} hodil {random.randint(1,6)}')

for hrac in range(0, 4): # range (od, do + 1)
    print(f'Hrac {hrac} hodil {random.randint(1,6)}')