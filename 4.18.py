s = '''It was the best of times, it was the worst of times; it
was the age of wisdom, it was the age of foolishness; it was the
epoch of belief, it was the epoch of incredulity; it was...'''

def Strip(txt) :
    txt =txt.replace('.', ' ')
    txt=txt.replace(',', ' ')
    txt=txt.replace(';',' ')
    newS = txt
    print(newS)

Strip(s)
