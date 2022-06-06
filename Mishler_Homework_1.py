from math import sqrt
from random import randint
#Problem 1
print (randint(1,10))
#Problem 2
for i in range(1,int(sqrt(10000))+1):
    print (i**2)
#Problem 3
abab = open("abab.txt", "r").readlines()[0]
print (len([_ for _ in filter(lambda x: x == 'b', abab)]))
#Problem 4
print (max(len(x) for x in abab.split('b')) - 1)
print (max(len(x) for x in abab.split('a')) - 1)
