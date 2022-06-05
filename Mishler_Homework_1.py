from random import randint
from math import sqrt
print (randint(1,10))
for i in range(int(sqrt(10000))+1):
    print (i**2)
abab = "aaabbbbbbbbbaaaabababbbbbaaaaaaaa"
print (len([_ for _ in filter(lambda x: x == 'b', abab)]))
print (max(len(x) for x in abab.split('b')) - 1)
print (max(len(x) for x in abab.split('a')) - 1)
