short = True
while short == True :
    stringlist = eval(input("give list with at least 10 strings: "))
    if len(stringlist) > 9 :
        short = False
listfour = []
for i in stringlist :
    if len(str(i)) == 4 :
        listfour.append(i)
print(listfour)
