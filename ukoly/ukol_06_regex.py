# 1. Pomocí nástroje regex101 vymysli regulární výraz, který označí platná data a neoznačí neplatná data:
# 
# platná data:
# 2.2.2022
# 13. 8. 1999
# 4/5/2001
# 
# neplatná data:
# 5.123.458.91
# 21.4
# 8./9

import re

regularni_vyraz = re.compile(r"\d?\d(\.|\/) ?\d?\d(\.|\/) ?\d{4}")
datum = input("Zadej datum: ")
test = regularni_vyraz.fullmatch(datum)

if test:
    print("OK")
else:
    print("Špatný formát vstupních dat!")

# 2. Zkopíruj si obsah souboru posta.txt do regex101 jako testovací řetězec. Vymysli regulární výraz, který označí všechny "poslední řádky adresy" v textu. Poslední řádka adresy zpravidla obsahuje PSČ a název obce, například 190 16 PRAHA 916 nebo 742 45 FULNEK. Celkem by jich mělo být 18.

regularni_vyraz_2 = re.compile(r"\d{3} \d{2} \w+ ?\w+ ?\w+")

# Nepovinný bonus
# Napiš program, který se zeptá uživatele na jeho přihlašovací jméno, e-mailovou adresu a heslo. Po každém zadaném údaji program ověří jeho správnost podle následujících pravidel:

# uživatelské jméno smí obsahovat malá a velká písmena (nesmí obsahovat žádné jiné znaky), jeho minimálná délka je 6 znaků a jeho maximální délka je 10 znaků.

# heslo smí obsahovat malá a velká písmena, číslice, a následující speciální znaky: _, -, ., +, =. Jeho minimálná délka je 12 znaků a jeho maximální délka je 30 znaků.

# e-mail by měl být validním e-mailem 🙂 Tady jsou nějaké testovací příklady (viz zdroj)

username = input("Zadej přihlašovací jméno nového uživatele (smí obsahovat malá a velká písmena, délka min. 6 a max. 10 znaků): ")
regex_username = re.compile(r"([a-zA-Z]{6,10})")
test_username = regex_username.fullmatch(username)

if test_username:
    useremail = input("Zadej svůj email: ")
    regex_useremail = re.compile(r"([A-Za-z0-9]+[.-_+])*[A-Za-z0-9-_+\"]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
    test_useremail = regex_useremail.fullmatch(useremail)

    if test_useremail:
        userpwd = input("Zadej heslo pro nového uživatele (smí obsahovat malá a velká písmena, číslice a speciální znaky '_' '-' '.' '+' '='. Délka 12-30 znaků.)")
        regex_userpwd = re.compile(r"[a-zA-Z0-9_\-\.\+\=]{12,30}")
        test_userpwd = regex_userpwd.fullmatch(userpwd)

        if test_userpwd:
            print("Uživatel úspěšně vytvořen!")
        else:
            print("Neplatný formát hesla!")

    else:
        print("Neplatný formát emailové adresy!")

else:
    print("Neplatné uživatelské jméno!")