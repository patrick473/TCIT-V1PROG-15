s = 'abcdefghijklmnopqrstuvwxyz'

a = s[1:3] == 'bc'


print(a)

b = s[:14] == 'abcdefghijklmn'

print(b)

c = s[14:] == 'opqrstuvwxyz'

print(c)

d = s[1:-1] == 'bcdefghijklmnopqrstuvwxy'

print(d)
