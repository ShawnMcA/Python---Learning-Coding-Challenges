# ========== Strings ========== #
strOriginal = 'Hello, my name is Shawn.'

# reverse string
print(strOriginal[:: -1])

# step through every other letter
print(strOriginal[::2])

# remove white spaces - replace
print(strOriginal.replace(' ', ''))

# remove white spaces - split/join
print(''.join(strOriginal.split(' ')))