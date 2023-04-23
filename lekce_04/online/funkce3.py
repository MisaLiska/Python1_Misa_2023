def get_mark(points):
    if points <= 60:
        mark = 5
    elif points <= 70:
        mark = 4
    elif points <= 80:
        mark = 3
    elif points <= 90:
        mark = 2
    else:
        mark = 1
    return mark

points = int(input("Zadej počet bodů v testu: "))
mark = get_mark(points)
print(f"Výsledná známka je {mark}.")

def get_mark(points, bonus=0):
    if points + bonus <= 60:
        mark = 5
    elif points + bonus <= 70:
        mark = 4
    elif points + bonus <= 80:
        mark = 3
    elif points + bonus <= 90:
        mark = 2
    else:
        mark = 1
    return mark

points = int(input("Zadej počet bodů v testu: "))
bonus = int(input("Zadej počet bonusových bodů: "))
mark = get_mark(points, bonus)
print(f"Výsledná známka je {mark}.")