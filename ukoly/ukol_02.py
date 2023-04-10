# Zadání
# Vyvíjíš software pro obchod s elektronickými součástkami. Firma eviduje informace o počtu součástek na skladě ve slovníku. Klíč slovníku je kód součástky a hodnota klíče je počet součástek na skladě.

# sklad = {
#   "1N4148": 250,
#   "BAV21": 54,
#   "KC147": 147,
#   "2N7002": 97,
#   "BC547C": 10
# }
# Napiš software, který bude využívat prodavač v případě, že do obchodu přijde zákazník. Software se nejprve zeptá na kód součástky a poté na množství, které si zákazník chce koupit. Obě informace si ulož. Následně naprogramuj následující varianty:

# Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.
# Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, že lze prodat pouze omezené množství kusů. Následně součástku odeber ze slovníku, protože je vyprodaná.
# Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši, a sniž počet součástek na skladě o množství požadované zákazníkem.

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
soucastka = str(input("Jakou součástku si zákazník přeje?: "))
if soucastka in sklad:
    pocet = int(input("Kolik kusů součástky si zákazník přeje?: "))
    if sklad[soucastka] >= pocet:
        print("Poptávku lze uspokojit v plné výši")
        sklad[soucastka] -= pocet
        print(f"Zůstatek na skladě {sklad}")
    else:
        print(f"Poptávku nelze uspokojit v plné výši, dostupný počet kusů pouze {sklad[soucastka]}")
        sklad.pop(soucastka)
        print(f"Zůstatek na skladě {sklad}")
else:
    print(f"Bohužel, součástka {soucastka} není momentálně na skladě.")
    
# Nepovinný bonus 1
# Ve slovníku zde najdeš Morseovu abecedu, kde jako klíč slouží znak v klasické abecedě a jako hodnota zápis znaku v Morseově abecedě.

# Napiš program, který se uživatele zeptá na text, který chce zapsat v Morseově abecedě. Uvažuj disciplinovaného uživatele, který zadává pouze znaky bez diakritiky, malá písmena atd. Na začátku uvažuj i to, že uživatel nezadává mezery.
# Projdi řetězec zadaný uživatelem. Najdi každý znak ve slovníku a vypiš ho na obrazovku v Morseově abecedě.
# Abychom měli celý kód vypsaný na jedné řádce, požádáme funkci print(), aby na konci výpisu nevkládala znak pro konec řádku, ale mezeru. To uděláme tak, že jako druhý argument funkce dáme argument end=" ".
# Nyní přidáme mezery. Uvažuj, že uživatel může zadat mezeru. Před tím, než budeš hledat znak ve slovníku, zkontroluj, zda znak není mezera. Pokud ano, vypiš znak lomítka /.