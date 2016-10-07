def rps():
    victory = False
    while victory == False :
        a = input('Player 1: R, P or S: ')
        b =input('Player 2: R, P or S: ')

        if (a == 'R' and b == 'S') or (a == 'S' and b == 'P') or (a == 'P' and b == 'R'):
            victory = True
            print('Player A has won')
        elif (b == 'R' and a == 'S') or (b == 'S' and a == 'P') or (b == 'P' and a == 'R'):
            victory = True
            print('Player B has won')
        else :
            print('Play again')

rps()
