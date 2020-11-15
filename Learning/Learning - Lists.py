# ========== Lists ========== # 
newList = [0, 25, 12, 34, 110, 43]

# Direct element access
print(newList[3]) # 34

# Access range of elements. Second index non-inclusive
print(newList[2:4]) # [12, 34]

# Empty second index to access remainder of list
print(newList[2:]) # [12, 34, 110, 43]

# Empty first index to get everything up to second index
print(newList[:3]) # [0, 25, 12]

# A step can be listed as well
print(newList[1::2])

# reverse a list
print(newList[::-1])


