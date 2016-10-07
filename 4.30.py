def distribution(name) :


    infile = open(name, 'r')
    content = infile.read()

    a = 0
    amin = 0
    bplus = 0
    b = 0
    bmin = 0
    c = 0
    cmin = 0
    f = 0

    a = content.count('A')
    amin = content.count('A-')
    bplus = content.count('B+')
    b = content.count('B')
    bmin = content.count('B-')
    c = content.count('C')
    cmin = content.count('C-')
    f = content.count('F')

    print(str(a) + ' Students got A')
    print(str(amin) + ' Students got A-')
    print(str(bplus) + ' Students got B+')
    print(str(b) + ' Students got B')
    print(str(bmin) + ' Students got B-')
    print(str(c) + ' Students got C')
    print(str(cmin) + ' Students got C-')
    print(str(f) + ' Students got F')

distribution('grades.txt')
