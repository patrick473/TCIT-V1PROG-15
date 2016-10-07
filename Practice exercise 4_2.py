
infile = open('kaartnummers', 'r')
content = infile.read()
wordList =content.splitlines()
content = str(wordList)
content = content.replace(']','')
content = content.replace('[','')
content =content.replace("'", "")
wordList = content.split(',')




naam = []
nummer = []
naam.append(wordList[1])
for i in wordList :

    if wordList.index(i) % 2 == 0 or wordList.index(i) == 0 :
        nummer.append(i)
    elif wordList.index(i) % 2 == 1 :
        naam.append(i)

naam.remove(naam[0])
print(wordList)
print(naam)
print(nummer)
for s in range(0,6,1):
    print(naam[s] + 'heeft kaartnummer: ' + nummer[s])

