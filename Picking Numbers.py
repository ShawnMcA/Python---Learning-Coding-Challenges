test = [4, 6, 5, 3, 3, 1]
# [1, 3, 3, 4, 5, 6]

def pickingNumbers(test):
    # Write your code here
    # longest subarray where absolute difference is 1 for all elements

    final = 0

    test.sort()
    
    for i in range(len(test) - 1):
        total = 1

        for j in range(i, len(test) - 1):
          if abs(test[i] - test[j + 1]) <= 1:
            total += 1

        if total > final: 
          final = total

    return final
    


print(pickingNumbers(test))