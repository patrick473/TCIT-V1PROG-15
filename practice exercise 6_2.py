def ticker(filename):
    infile = open(filename)
    tickers = infile.read()
    nticker = []
    nnticker = {}
    ticker = tickers.splitlines()
    for i in ticker:
        nticker.append(i.split(':'))

    nnticker.update(nticker)


    inputt = input('Enter company name: ')

    if inputt in nnticker.keys():
        print(nnticker[inputt])
    if inputt in nnticker.values():
        for comp,abb in nnticker.items():
            if abb == inputt :
                print(comp)
ticker('tickers')
