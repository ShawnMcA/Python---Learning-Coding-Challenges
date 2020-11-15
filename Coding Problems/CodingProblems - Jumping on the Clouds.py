'''
  Sequentially numbered clouds
  Either thunderheads or cumulus clouds
  jump from cloud to cloud 


  Given array of clouds, energy level
  Takes 1 energy to make k sized jump
  Starts on c[0]
  If the element she lands on is a 1 aka
    a thundercloud she loses an additional 2
    energy
  game ends when she lands back on cloud 0

  c = cloud array
  e = 100 = energy level
  k = jump size


'''
n = 8
k = 3
c = [1, 1, 1, 0, 1, 1, 0, 0, 0, 0]

def jumpingOnClouds(c, k):
  energy = 100

  for i in range(k, len(c) + 1, k):
    if i == len(c):
      i = 0

    if c[i] == 1:
      energy -= 3
    else:
      energy -= 1
  
  return energy

print(jumpingOnClouds(c, k))