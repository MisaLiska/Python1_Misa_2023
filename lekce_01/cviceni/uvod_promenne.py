# number_of_tickets = input("Kolik si přejete lístků? ")
# price_per_ticket = 345
# total_price = number_of_tickets * price_per_ticket
# print(total_price)

# number_of_tickets = input("Kolik si přejete lístků? ")
# price_per_ticket = 345
# number_of_tickets = int(number_of_tickets)
# total_price = number_of_tickets * price_per_ticket
# print(total_price)

# Námět: Zkus spojit funkce input a int do jedné, tj. napiš obě funkce do jednoho řádku. Tím program zkrátíš a zpřehledníš.

# number_of_tickets = int(input("Kolik si přejete lístků? "))
# price_per_ticket = 345
# total_price = number_of_tickets * price_per_ticket
# print(total_price)

play = "Každý má svou pravdu"
number_of_tickets = int(input("Kolik si přejete lístků? "))
price_per_ticket = 345
total_price = price_per_ticket * number_of_tickets

print("Cena " + str(number_of_tickets) + " lístků na hru " + play + " je celkem " + str(total_price) + " Kč.")

print(f"Cena {number_of_tickets} lístků na hru {play} je celkem {total_price} Kč.")
