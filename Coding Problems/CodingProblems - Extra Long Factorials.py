'''
  Return the factorial of large number
'''

def extraLongFactorials(n):
    if n == 1: 
        return n
    
    return n * extraLongFactorials(n - 1)
  
print(extraLongFactorials(4))