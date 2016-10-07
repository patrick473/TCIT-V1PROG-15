def week():
    weekdays = {'mo':'monday','tu':'tuesday','we':'wednesday','th':'thursday','fr':'friday','sa':'saturday','su':'sunday'}
    another = True
    while another == True :
        inputt = input('Enter day abbreviation: ')
        if inputt != '' :
            print(weekdays[inputt])
        else:
            another = False


week()
