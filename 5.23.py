def pay(hours,wage) :

    if  40 < hours > 60 :
        hours -= 40
        pay = wage * 40

        pay = pay + (hours * (wage * 1.5))

    elif hours > 60 :
        hours -=60
        pay = wage * 40
        pay = pay +((wage * 1.5) * 20)

        pay = pay + (hours * (wage * 2))
    else: # hours <40
        pay = hours * wage
    print(pay)

pay(40,10) # expect 100
pay(60,10) # expect 550
pay(80,10) # expect 850
