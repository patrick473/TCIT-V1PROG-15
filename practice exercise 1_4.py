cijferICOR = 6.2
cijferPROG = 7.5
cijferCSN = 6.7

sum = (cijferICOR + cijferPROG + cijferCSN)
gemiddelde = sum/3
beloning = gemiddelde * 30

overzicht = ('Mijn cijfers (Gemiddeld een ' + str(gemiddelde) + ') leveren een beloning van € ' + str(beloning) + ' op.')

print(overzicht)

