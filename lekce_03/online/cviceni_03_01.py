import json

with open('lekce_03/online/zavod.json', encoding='utf-8') as file:
    runners = json.load(file)
winner = runners[0]
winner_time = winner["casy"]["oficialni"]
print(f"Vítězem se stal {winner['jmeno']}, s časem {winner_time}, velká gratulace!!")

finishers = []
# print(type(finishers))

for runner in runners:
    if runner['casy']['oficialni'] != 'DNF':
        finishers.append(runner['jmeno'])

print(f"Dokončili: {finishers}")
print(f"Stříbrná medajle pro {finishers[1]}, rovněž gratulujeme!")
    