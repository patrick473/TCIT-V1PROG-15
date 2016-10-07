def namen():
    newInput = True
    names = {}
    namesList = []
    while newInput == True:
        inputt = input('Volgende naam: ')
        if inputt in names.keys():
            names[inputt] += 1
        elif inputt == '' :
            newInput = False

        else :
            names[inputt] = 1
            namesList.append(inputt)
    for i in namesList :
        if names[i] == 1 :
            print('There is ' + '1' + ' student named '+ i)
        else :
            print('There are ' + str(names[i]) + ' students named ' + i)


namen()
