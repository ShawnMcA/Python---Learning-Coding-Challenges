# 
n = 7
m = 19
s = 2


def saveThePrisoner(n, m, s):

    # n number of prisoners
    # m number of sweets to pass out
    # s chair number to begin with
    
    piecesToHandOut = ((m - 1) % n)
    
    if piecesToHandOut + s <= n:
        return piecesToHandOut + s
    elif piecesToHandOut + s > n:
        return piecesToHandOut + s - n
    

print(saveThePrisoner(n, m, s))
