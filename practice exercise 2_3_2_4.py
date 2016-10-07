leeftijd = input('Geef je leeftijd: ')
paspoort = input('Heb je een nederlands paspoort: ')

if (paspoort == 'ja')and (int(leeftijd) == 18 or int(leeftijd) > 18) :
    print('Gefeliciteerd, je mag stemmen!')
else :
    print('Jammer, je mag niet stemmen!')
