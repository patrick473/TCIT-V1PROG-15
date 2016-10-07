stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "'s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

beginstation =input('Wat is je beginstation? : ')


if beginstation not in stations :
    print('Sorry dit station komt niet voor in treintraject Schagen-Maastricht')
    beginstation = 'Schagen'
eindstation = input('Wat is je eindstation? : ')
if eindstation not in stations :
    print('Sorry dit station komt niet voor in treintraject Schagen-Maastricht')
    eindstation = 'Maastricht'
if int(stations.index(eindstation)) < int(stations.index(beginstation)) :
        print('Het eindstation is eerder dan het beginstation het eindstation is nu Maastricht')
        eindstation = 'Maastricht'
afstand = (int((stations.index(eindstation)) - int(stations.index(beginstation))  ))
ritprijs = afstand * 5
rangnummerb = stations.index(beginstation) + 1
rangnummere = stations.index(eindstation) + 1
print('Beginstation is : ' + str(beginstation) + '. Dit station heeft als rangnummer: ' + str(rangnummerb))
print('Eindstation is : ' + str(eindstation) + '. Dit station heeft als rangnummer: '+ str(rangnummere))
print('De afstand is: ' + str(afstand) + ' stations')
print('Het kost je: ', str(ritprijs) + ' euro om van ' + str(beginstation) + ' naar ' + str(eindstation) + ' te komen' )
while (rangnummerb < rangnummere) :
    print(stations[rangnummerb])
    rangnummerb = rangnummerb+1
