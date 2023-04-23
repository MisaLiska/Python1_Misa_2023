# Napiš funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek.

def mult(a, b):
    """
    Popis funkce
    """
    nasob= a * b
    return nasob

a = int(input("Zadej první číslo: "))
b = int(input("Zadej druhé číslo: "))
vysledek = mult(a, b)
print(f"Výsledek je {vysledek}")