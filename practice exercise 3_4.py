def new_password(oldpassword, newpassword) :

    bevatnummer = 'False'

    for i in newpassword:
        if i in '0123456789':
            bevatnummer = 'True'
            break


    goedPassword = (newpassword != oldpassword) and (len(newpassword) >= 6) and (bevatnummer == 'True' )
    print(goedPassword)

new_password('jan','janje7')
