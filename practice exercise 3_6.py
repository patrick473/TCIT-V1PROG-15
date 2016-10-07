def wijzigLijst(letterlijst) :
    print(letterlijst)
    while len(letterlijst) > 0 : letterlijst.pop()
    letterlijst.append('d')
    letterlijst.append('e')
    letterlijst.append('f')
    print(letterlijst)

wijzigLijst(['a', 'b', 'c'])

def wijzigString(letter) :
    letter = 'd'
    print(letter)
wijzigString('a')
