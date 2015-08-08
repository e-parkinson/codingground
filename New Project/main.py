
def calcProbPos(bPlus,bMinus,cPlus,cMinus):
    probPos = ((bPlus/cPlus)*(cPlus/(cPlus+cMinus)))/((bPlus+bMinus)/(cPlus+cMinus))
    return probPos

corpora = open('sampleCorpora.txt')

print('Enter a statement without punctuation:')
userStatement = input().lower()
userStatement = userStatement.strip('\n').split(' ')

lengthInput = userStatement.length()
for n in range(0,lengthInput):
    checkString = userStatement[n]
    print(checkString)