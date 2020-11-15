newSet = { 0, 24, 'shawn', 25 }

# print out all elements of list
for elem in newSet:
  print(elem)

# check if element in Set
if 'shawn' in newSet:
  print(True)

def extraLongFactorials(n):
    if n == 0: 
        return n
    
    return extraLongFactorials(n - 1)

print(extraLongFactorials(3))