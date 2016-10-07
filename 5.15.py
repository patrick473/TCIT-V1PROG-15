def vowels(input):
    for char in input:
        if char in 'aeiouAEIOU' :
            indexlist.append(input.index(char))
        else :
            continue
    print(indexlist)

indexlist = []

vowels('Hello WORLD')
