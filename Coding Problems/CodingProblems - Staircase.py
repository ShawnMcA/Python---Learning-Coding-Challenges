n = 4

def staircase(n):
  for i in range(1, n + 1):
    tempArray = []

    for j in range(0, n):

      if((j + i) >= n):
        tempArray.append('#')
      else:
        tempArray.append(' ')
            
    print(''.join(tempArray))

staircase(n)