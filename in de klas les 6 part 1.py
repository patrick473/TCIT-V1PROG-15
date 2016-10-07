cursus = {'jan':5.1,'piet':9.1,'kees':8.3,'inge':9.3,'loes':6.1,'ahmed':5.4,'sara':6.1,'klaas':4.3}


for naam in cursus.keys():
    print(naam, end = '\n')
print('\n')

for cijfers in cursus.values():
    print(cijfers, end='\n')

for naam in cursus.keys():
    print(naam, cursus[naam])
