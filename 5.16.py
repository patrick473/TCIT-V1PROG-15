'''
def indexes(word, character):
   for char in word:
        charlist[char.index(str(char))] = char
        for i in charlist :
            if i == character :
                n = charlist.index(i)
                print(n)
                indexlist[indexlist.index(str(n))] = n





   print(indexlist)
   indexlist.clear()
indexlist = []
charlist = []

indexes('mississippi', 's')
indexes('mississipi', 'i')
indexes('mississipi', 'a')
'''
