import random
def monopolyworp() :
    worp = True
    dubbel = 0
    while worp == True:
      a = random.randint(1,6)
      b = random.randint(1,6)
      c = a+b
      if dubbel > 2 :
        print(str(a) + ' + ' + str(b) + ' = (direct naar gevangenis)')
        worp = False
        break

      if a == b :
        print(str(a) + ' + ' + str(b) + ' = ' + str(c) + ' (dubbel)')
        dubbel += 1
      else :
        print(str(a) + ' + ' + str(b) + ' = ' + str(c))
        worp = False

monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
