a = 'abc'
b = 'dna'
def rev(a) :

   if len(a) <= 1:
        return a

   return rev(a[1:]) + a[0]

print(rev('abc'))
print(rev('dna'))

