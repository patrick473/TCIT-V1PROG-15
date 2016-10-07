number = 1
sum = 0
counter = 0
while int(number) != 0 :
    number = input('Give a number: ')
    sum = int(sum) + int(number)
    counter += 1
counter =counter - 1
print('There have been ' + str(counter)+ ' numbers given, and the sum of all the numbers is: '+ str(sum))

