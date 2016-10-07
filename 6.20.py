def reverse(dict):

    dictr = {}
    key = ''
    value = ''
    for i in dict.keys():
        v = dict[i]
        key = v
        value = i
        dictr[v] = i
    print(dictr)




phonebook = {'Smith, Jane':'123-45-67', 'Doe, John':'987-65-43','Baker,David':'567-89-01'}

reverse(phonebook)
