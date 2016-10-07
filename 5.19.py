def inBoth(a,b) :

    for i in a :

        for u in b :
            if i !=u :
                continue
            else :
                both.append(int(i))
    print(both)

both = []

inBoth([1,2,3,4,10,9,7],[1,2,3,4,5,6,7])
