def censor(file) :
    infile = open(file, 'r+')
    content = infile.read()
    wordList = content.split(' ')
    for i in wordList :
        if len(i) == 4 :
            i = 'XXXX'

    content = ''.join(wordList)
    infile.write(content)

censor('censor')

