vysvedceni = {
    "cesky_jazyk" : 4,
    "matematika" : 3,
    "dejepis" : 2
}
print(vysvedceni)

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
print(sales)
sales["Noc, která mě zabila"] = 0
sales["Vrah zavolá v deset"] = sales["Vrah zavolá v deset"]+100
print(sales)

tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor 7",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}
listek = int(input("Jaké je Tvé číslo lístku? "))
if listek in tombola:
    print(f"Dnes vyhřáváš {tombola[listek]}")
else:
    print("Tak dneska bohužel nic")

passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}
jmeno = input("Řekni to jméno! ")
if jmeno in passwords.keys():
    heslo = input("Řekni to heslo! ")
        if heslo in passwords.values():
            print("You may enter")
        else:
            print("Táhni!")
else:
    print("Táhni socko!")