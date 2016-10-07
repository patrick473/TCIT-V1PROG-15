def convert(celcius) :
    return  ((celcius * 1.8) + 32)
def table() :
    print('  F      C')
    for i in range(-30,40,10):



        print('{0}     {1}'.format(convert(i), i,))

table()

