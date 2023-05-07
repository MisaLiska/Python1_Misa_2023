# Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

# Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
# Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
# Tvůj program bude obsahovat dvě funkce:

# První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.

# Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.

# Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

# Tipy:

# Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili.
# Pro kontrolu předvolby použijte slicing (viz první lekce) pro získání prvních 4 znaků řetězce. Ty porovnejte s řetězcem "+420".

# Nepovinný bonus 1
# Zkus svoji první funkci upravit tak, že si bude umět poradit s mezerami v telefonním čísle. Mezer se zbavíš například tak, že použiješ metodu .replace(). První parametr metody replace je znak, který chceš nahradit, a druhý parametr nový znak. Pokud se chceš nějakého znaku zbavit, "nahraď" ho prázdným řetězcem "".

# Odkaz na dokumentaci metody replace: https://docs.python.org/3/library/stdtypes.html#str.replace

# Nepovinný bonus 2
# Přidej svým funkcím typování, aby bylo jasné, jaký typy mají parametry tvých funkcí a jaká je návratová hodnota tvých funkcí.

def kontrola_cisla(vstup:str) -> bool:
    """
    Funkce detekuje spravny format zadaneho cisla pro odeslani sms.
    Funkce vraci False / True
    """
    cislo:str = ""
    cislo = vstup.replace(" ", "")

    if len(cislo) == 9:
        return True
    elif len(cislo) == 13:
        return True
    else:
        return False

def cena_sms(text:str) -> float:
    """
    Funkce spocita delku zpravy a rozdeli na zpravy po 180 znacich.
    Funkce vraci pocet zprav.
    """
    pocet_znaku:int = len(text)
    pocet_zprav:int = 0
    if pocet_znaku < 180:
        pocet_zprav = 1
    elif pocet_znaku % 180 == 0:
        pocet_zprav = pocet_znaku / 180
    else:
        pocet_zprav = (pocet_znaku // 180) + 1
    cena:float = pocet_zprav * 2.5
    return cena

cislo_sms:str = input("Zadej telefonní číslo: ")
if kontrola_cisla(cislo_sms):
    text_sms:str = input("Zadej text: ")
    print(f"Vaše zpráva byla odeslána, cena je {cena_sms(text_sms)} Kč")
else:
    print("Špatný formát čísla")

