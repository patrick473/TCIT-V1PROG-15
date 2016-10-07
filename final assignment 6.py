def code(invoerString):
    new = ''
    for i in invoerString :
        char = chr(ord(i) + 3)
        new = new + str(char)
    print(new)
    return new

code(input('Voer een woord in: '))

