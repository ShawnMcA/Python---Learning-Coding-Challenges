arr = ['4', '3', '5', '1', '2']

def sequenceEquation(arr):
    
    for i in range(1, len(arr) + 1):
        num = arr.index(str(i)) + 1
        print(arr.index(str(num)) + 1)
        
sequenceEquation(arr)