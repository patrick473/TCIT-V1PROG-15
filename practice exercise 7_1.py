prijs = 4356.0
continu = False

try:

    personen = int(input('Met hoeveel mensen ben je?: '))
    if personen < 0 :
        print('Delen door negatieve getallen kan niet')
    else:
        print('de reis kost per persoon ' + str(prijs/personen) + ' euro')

except ValueError :
    print('Gebruik cijfers voor het invoeren an het aantal')
except ZeroDivisionError :
    print('Delen door 0 kan niet')
except RuntimeError :
    print('Onjuiste invoer')
