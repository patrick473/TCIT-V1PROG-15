i = ''
while len(i) != 4 :
    i = input('Geef een string van vier letters: ')
    if len(i) != 4 :
        print(i + ' heeft ' + str(len(i)) + ' letters')
    else :
        print('inlezen van correcte string: ' + i + ' is geslaagd')
        break
