stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "'s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']


def inlezen_beginpunt() :

    beginstation = ''
    while beginstation not in stations :
        beginstation = input('wat is je beginstation? : ')
    return beginstation

def inlezen_eindpunt(begin) :

    eindstation =  ''

    while eindstation not in stations or int(stations.index(eindstation)) < int(stations.index(begin))  :
        eindstation = input('wat is je eindstation? : ')
    return eindstation

def omroepen_reis(begin, eind):
    afstand = int(stations.index(eind)) - int(stations.index(begin))
    ritprijs = afstand * 5
    rangnummerb = stations.index(begin) + 1
    rangnummere = stations.index(eind) + 1
    print('Beginstation is : ' + str(begin) + '. Dit station heeft als rangnummer: ' + str(rangnummerb))
    print('Eindstation is : ' + str(eind) + '. Dit station heeft als rangnummer: '+ str(rangnummere))
    print('De afstand is: ' + str(afstand) + ' stations')
    print('Het kost je: ', str(ritprijs) + ' euro om van ' + str(begin) + ' naar ' + str(eind) + ' te komen' )
    while (rangnummerb < rangnummere) :
        print(stations[rangnummerb])
        rangnummerb = rangnummerb+1


begin =inlezen_beginpunt()
eind = inlezen_eindpunt(begin)
omroepen_reis(begin, eind)
