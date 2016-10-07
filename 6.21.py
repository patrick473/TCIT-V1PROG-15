def ticker(filename):
    infile = open(filename)
    tickers = infile.read()
    nticker = []

    ticker = tickers.splitlines()
    for i in ticker:
        nticker.append(i.split(':'))



    i = iter(tuple(nticker))
    nnticker = dict(zip(i,i))
    print(nnticker)
    inpu = input('Enter company name: ')
    if inpu in nnticker:
        print('ticker symbol: '+ nnticker.values(inpu))
ticker('tickers')
