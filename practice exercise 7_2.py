import datetime
import csv
bestand = open('inloggers.csv','w')

with open('inloggers.csv','w', newline='') as bestand:
    writer = csv.writer(bestand, delimiter=';')

    while True:
        naam = input("Wat is je achternaam? ")
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        time = datetime.datetime.now().time()
        timing = datetime.datetime.now()
        timinge = ('%s' % timing)
        writer.writerow((timinge,voorl,naam,gbdatum,email))
        break

