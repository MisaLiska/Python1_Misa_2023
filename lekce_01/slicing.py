pohyby = [1200, -250, -800, 540, 721, -613, -222]
print(pohyby[2])
print(pohyby[2:])
print(f"Počet transakcí: {len(pohyby)}")
print(f"Nejvetší výdaj: {min(pohyby)}, největší příjem {max(pohyby)}")
print(f"Celková bilance za období: {sum(pohyby)}")
print(f"Průměrný pohyb {sum(pohyby)/len(pohyby)}")