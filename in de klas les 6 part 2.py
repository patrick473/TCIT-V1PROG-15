zin = 'all animals are equal but some animals are more equal than other' \

woorden = zin.split()

woordenteller = {}

for woord in woorden:
    if woord in woordenteller.keys():
        woordenteller[woord] += 1
    else:
        woordenteller[woord] = 1

for woord in woordenteller.keys():
    print(woord + '     komt ' + str(woordenteller[woord]) + ' keer voor.')
