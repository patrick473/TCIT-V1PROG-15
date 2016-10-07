

def stats() :

    infile = open('loremipsum.txt', 'r')
    content = infile.read()
    lines = content.count('\n')
    print(lines)
    wordList = content.split()
    print(len(wordList))
    char = 0
    for i in content :
        char += 1
    print(char)
stats()
