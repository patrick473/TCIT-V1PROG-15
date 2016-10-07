infile = open('kaartnummers')
content = infile.read()
lines = content.count('\n')

wordList = content.splitlines()
content = str(wordList)
content = content.replace(']','')
content = content.replace('[','')
content =content.replace("'", "")
wordList = content.split(',')


nummer = []
for i in wordList :

    if wordList.index(i) % 2 == 0 or wordList.index(i) == 0 :
        nummer.append(i)

biggestNumber = 0
line = 0
for u in range(0,6) :
    line += 1

    if  int(nummer[u]) > biggestNumber:
        biggestNumber = int(nummer[u])


print('Deze file telt ' + str(lines) + ' regels')
print('Het grootste kaartnummer is: ' + str(biggestNumber) + ' en dat staat op regel ' + str(line))
