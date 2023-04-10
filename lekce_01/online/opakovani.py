print("Vítejte v dlouhodobém kurzu Pythonu")
nazev_hry = "Romeo a Julie"
cena_listku = 150
vek = int(input("Zadej svůj věk: "))
if vek >= 13:
    pocet_listku = int(input("Zadej počet lístků: "))
    celkova_cena = cena_listku * pocet_listku
    #print("Cena všech lístků je", celkova_cena)
    if pocet_listku >= 4:
        #zlevnena_cena = celkova_cena * 0.9
        #print(f"Zlevněná cena je {zlevnena_cena} z původní {celkova_cena}")
        zlevnena_cena = celkova_cena - cena_listku
        print(f"Máš jeden lístek zdarma!. Zlevněná cena je {zlevnena_cena} z původní {celkova_cena}")
    else:
        print(f"Cena všech lístků je {celkova_cena}")
else:
    print(f"Dej si odchod mladej a vrať se, až Ti bude aspoň 13!")