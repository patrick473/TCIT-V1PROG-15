def easyCrypto(word) :
    new = ''
    for i in word :
        if  ord(i) % 2 == 0 :

            char = chr(ord(i) + 1)
            new = new + str(char)
        else :
            char = chr(ord(i)-1)
            new = new + str(char)
    print(new)

easyCrypto(input())
