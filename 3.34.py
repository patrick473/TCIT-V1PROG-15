def pay() :
    wage = input('How much is your hourly wage? :')
    hour = input('How many hours do you work in a week :')

    if int(hour) > 40 :
        base = float(wage) * 40
        overhour = int(hour) - 40
        pay = base + (overhour * (float(wage) * 1.5))
    else :
        pay = int(hour) * float(wage)

    print('You are earning ' + str(pay) + ' $ a week.')

pay()
