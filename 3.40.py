def partition() :
    print('Enter 5 last names of soccer player:')
    a = input()
    b = input()
    c = input()
    d = input()
    e = input()
    soccer = [a, b, c, d, e]

    for i in soccer :
        if i[0] in 'abcdefghijklmABCDEFGHIJKLM' :
            print(str(i))

partition()
