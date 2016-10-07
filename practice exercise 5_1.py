def season(monthnumber):
    month = ''
    if str(monthnumber) in '345' :
        month = 'spring'
    elif str(monthnumber) in '678' :
        month = 'summer'
    elif monthnumber == 9 or monthnumber == 11 or monthnumber == 10:
        month = 'fall'
    elif monthnumber == 1 or monthnumber == 2 or monthnumber == 12 :
        month = 'winter'
    print(month)


season(1)
season(4)
season(7)
season(10)
