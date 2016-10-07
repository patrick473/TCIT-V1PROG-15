def standaardprijs(afstandKM) :
    if afstandKM < 0 :
        afstandKM = 0

    if afstandKM > 50 :
        tarief = (15 + (afstandKM * 0.6))
    else :
        tarief = afstandKM * 0.8
        return(tarief)

def ritprijs(leeftijd, weekendrit, afstandKM) :
    tarief = standaardprijs(afstandKM)
    korting = 1
    if leeftijd <= 11 or leeftijd >= 65 :
        if weekendrit is True :
            korting = 0.65
        else :
            korting = 0.7
    else :
        if weekendrit is True :
            korting = 0.6



    prijs = tarief * korting
    return round(prijs, 2)

leeftijden = [11,12,64,65]
afstand = [-1,49,50]

for age in leeftijden :
    for distance in afstand :
        print(str(age) + ' '+str(distance) + ' True ' + str(ritprijs(age,True,distance)))
        print(str(age) +' '+ str(distance) + ' False ' + str(ritprijs(age,False,distance)))
