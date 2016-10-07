lst = [2,3,4,5]

def a(aa) :
    aa.sort()
    return aa
def b(aa,bb):
    aa.append(bb)
    return aa
def c(aa,cc):
    ccc = aa.count(cc)
    return ccc
def d(aa,dd,ee):
   aa.insert(dd,ee)
   return aa

print(a(lst))
print(b(lst,3))
print(c(lst,3))
print(d(lst,2,1))
