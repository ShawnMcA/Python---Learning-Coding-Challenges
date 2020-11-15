import math

s = 'haveaniceday'

def encryption(s):
    strArray = list(s)

    sqrCeil = math.ceil(math.sqrt(len(strArray)))
    
    newArray = []

    for i in range(sqrCeil):
        string = ''
        for j in range(i, len(strArray), sqrCeil):
            string += strArray[j]
        newArray.append(string)
    
    return ' '.join(newArray)
