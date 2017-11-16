#Erik Hansen
#11/16/17
#warmup13.py
from random import randint
list1 = []
for i in range(1,21):
    list1.append(randint(1,100))
    
print(min(list1))
print(max(list1))
print(sum(list1))
