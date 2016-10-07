import csv
from collections import defaultdict

columns = defaultdict(list)
numbers = []
with open('practice exercise73.csv') as text:
    reader = csv.reader(text,delimiter=';')
    for row in reader:
        for (i,v) in enumerate(row):
            columns[i].append(v)
    numbers = columns[2]
    namen = columns[0]
    datum = columns[1]
    print(numbers)
    hoogste = max(numbers)
    hoogsteNaam = namen[numbers.index(str(hoogste))]
    hoogsteDatum = datum[numbers.index(str(hoogste))]
    print('De hoogste score is: '+ hoogste+' op '+ hoogsteDatum + ' behaald door '+ hoogsteNaam)
