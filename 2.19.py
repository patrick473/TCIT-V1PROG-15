answers = ['y','n','n','y','n','y','y','y','n','n','n']

numYes = answers.count('y')
numNo = answers.count('n')
percentYes = (numYes / len(answers)) *100
print(answers)
print(answers.index('y') )
answers.sort()

print(answers)

print(answers.index('y')  )
print(numYes)
print(numNo)
print(percentYes)
