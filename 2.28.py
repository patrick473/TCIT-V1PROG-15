lst = [1,2,3,5,46,2,3,1,5,6,7,0,4,78,9,4,4,2,6,7,8]
a = int((len(lst) / 2) + 1)
print(a)
b = type(lst[a])
print(b)
#C
lst.sort(reverse=True)
print(lst)

d = lst[0]
lst.append(d)
lst.remove(lst[0])
print(lst)
