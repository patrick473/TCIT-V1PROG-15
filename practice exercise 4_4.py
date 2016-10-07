import time
infile = open('hardlopers', 'a')

def add() :
    name = input('Naam hardloper: ')
    infile.write(time.strftime('%A %b/%d/%y %I:%M %p', time.localtime())+ ', ' + name + '\n')
new = True


while new == True :
    add()
    if str(input('Wil je nog een hardloper invoeren?: (Y or N)')) == 'N' :
        new = False
