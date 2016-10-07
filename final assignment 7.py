import csv
import random
from collections import defaultdict

columns = defaultdict(list)
with open('kluizen.csv') as text:
    reader = csv.reader(text,delimiter=';')
    for row in reader:
        for (i,v) in enumerate(row):
            columns[i].append(v)
    kluizenGebruikt = columns[0]
    for u in kluizenGebruikt:
        kluizenGebruikt[kluizenGebruikt.index(u)] = int(u)



def code() :
    rand  =random.choice('0123456789')
    rand1 =random.choice('0123456789')
    rand2 =random.choice('0123456789')
    rand3 =random.choice('0123456789')
    code = str(rand+rand1+rand2+rand3)
    return code
def kluis_openen():
    with open('kluizen.csv') as text:
        reader = csv.reader(text,delimiter=';')
        for row in reader:
            for (i,v) in enumerate(row):
                columns[i].append(v)
        codes = columns[1]
        kluisNummers = columns[0]
    i = False
    while i == False :
        codeInput = input('Wat is je code?')
        if codeInput in codes :
            for j in codes :
                if j == codeInput :
                    k = kluisNummers[codes.index(j)]

                    print('Kluis nummer '+ str(k) + ' wordt geopend')
                    i = True
                    break
        else:
            print('Dit is geen goede code')


def beschikbaar():
    csvfile = open('kluizen.csv', 'r', newline='')
    reader = csv.reader(csvfile)
    nietBeschikbaar = 0
    for row in reader:
        nietBeschikbaar = nietBeschikbaar + 1
    return (12-nietBeschikbaar)
def aantal_kluizen_vrij():
    print('Er zijn '+str(beschikbaar())+ ' kluisjes vrij')
def nieuweKluis():

    with open('kluizen.csv') as text:
        reader = csv.reader(text,delimiter=';')
        for row in reader:
            for (i,v) in enumerate(row):
                columns[i].append(v)

    if beschikbaar() > 0 :
        for i in range(1,13):
            dichteKluizen = columns[0]
            if str(i) not in dichteKluizen:
                openKluis = i


                password = code()
                with open('kluizen.csv','a',newline='') as text:
                    writer = csv.writer(text, delimiter=';')
                    writer.writerow((openKluis,password))
                print('Jouw kluis is nummer ' + str(i) + ' en de code voor deze kluis is ' + password)
                break
    else :
        print('er zijn geen kluizen beschikbaar')











while True :
    print('1: ik wil een nieuwe kluis')
    print('2: ik wil mijn kluis openen')
    print('3: ik geef mijn kluis terug')
    print('4: ik wil weten hoeveel kluizen nog vrij zijn')
    print('5: ik wil stoppen')
    try :
        invoer = int(input())
    except:
        print('kies uit 1 t/m 5')
        continue

    if invoer > 5 :
        print('kies uit 1 t/m 5')
        continue
    elif invoer == 5 :
        break
    elif invoer == 4 :
        aantal_kluizen_vrij()
    elif invoer == 3 :
        print('nog niet beschikbaar')
    elif invoer == 2:
        kluis_openen()
    elif invoer == 1:
        nieuweKluis()
