from xml.dom import minidom
xmldoc = minidom.parse('inalassignment8')
synoniemen = xmldoc.getElementsByTagName('Synoniem')


syna = []
synb = {'Synoniemen':syna}



codes = xmldoc.getElementsByTagName('Code')
types = xmldoc.getElementsByTagName('Type')
langs = xmldoc.getElementsByTagName('Lang')
codea = []
typea = []
langa = []

for i in synoniemen:
    syna.append(i.childNodes[0].nodeValue)
for i in codes:
    codea.append(i.childNodes[0].nodeValue)
for i in types :
    typea.append(i.childNodes[0].nodeValue)
for i in langs :
    langa.append(i.childNodes[0].nodeValue)

codetype = dict(zip(codea,typea))
codelang = dict(zip(codea,langa))

print('Dit zijn de codes en types van de 4 stations:')
for u,i in codetype.items():
    print('{}   - {}'.format(u,i))

print('Dit zijn alle stations met een of meer synoniemen:')
print(synb)

print('Dit is de langste naam van elk station:')
for u,i in codelang.items():
    print('{}   - {}'.format(u,i))
