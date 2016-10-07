import csv
from collections import defaultdict

columns = defaultdict(list)

with open('practice exercise74.csv') as text:
    reader = csv.reader(text,delimiter=';')
    next(reader,None)
    for row in reader:
        for (i,v) in enumerate(row):
            columns[i].append(v)
vooraad = columns[3]
prijs = columns[4]
artikelnummer = columns[0]
naam = columns[2]

for u in prijs :
    prijs[prijs.index(u)] = float(u)
for y in vooraad :
    vooraad[vooraad.index(y)] = int(y)
hoogstePrijs = max(prijs)
hoogsteProduct = naam[prijs.index(hoogstePrijs)]
laagsteVooraad = min(vooraad)
laagsteVooraadProduct = artikelnummer[vooraad.index(laagsteVooraad)]
totaal = 0
for j in vooraad :
    totaal = totaal + int(j)

print('Het duurste artikel is '+ str(hoogsteProduct) + ' en die kost '+ str(hoogstePrijs)+ ' euro')
print('Er zijn slechts '+ str(laagsteVooraad) + ' exemplaren in voorraad van het product met nummer '+ laagsteVooraadProduct)
print('In totaal hebben wij '+ str(totaal) + ' producten in ons magazijn liggen')
