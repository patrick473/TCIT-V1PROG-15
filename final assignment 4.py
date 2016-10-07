annuleringen = open('annuleringen')
treinritten = open('treinritten')
cAnnuleringen = annuleringen.read()
cTreinritten = treinritten.read()

annuleringList = cAnnuleringen.splitlines()
cAnnuleringen = str(annuleringList)
annuleringList = cAnnuleringen.replace('Annulering: ','')

treinrittenList = cTreinritten.splitlines()
treinrittenListStation = []
for i in treinrittenList:
    iNew = i.rstrip().split('- ')[1]
    if annuleringList.count(iNew) == 0:
        treinrittenListStation.append(i)
infile = open('correcteTreinRitten', 'w')
for i in treinrittenListStation :
    infile.write('{}\n'.format(i))



