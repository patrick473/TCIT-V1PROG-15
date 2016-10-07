def average () :
    sentence = input('Enter a sentence: ')
    woorden = sentence.split()
    a = 0
    for i in woorden :
        a = a+ len(i)
    a = a / len(woorden)
    print(a)
average()
