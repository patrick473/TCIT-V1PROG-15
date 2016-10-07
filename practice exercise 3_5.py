import math
def kwadraten_som(grondgetallen) :
    for i in grondgetallen :
        if i < 0 :
            grondgetallen.remove(i)
    return sum([grondgetal**2 for grondgetal in grondgetallen ])



print(kwadraten_som([4,5,3,-81]))

