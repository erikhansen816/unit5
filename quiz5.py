#Erik Hansen
#12/4/17
#quiz5.py

from random import randint

def rand5():
    l1 = []
    for i in range(1,6):
        l1.append(randint(1,100))
    return(l1)

def lastElement(A):
    return(A[len(A)-1])
    
def wordLengths(B):
    B1 = []
    for i in B:
        B1.append(len(i))
    return(B1)

def biggest(C):
    C1 = C[0]
    for i in C:
        if i>C1:
            C1 = i
    return C1
        

print(rand5())
print(lastElement(['cat','dog','rat']))
print(wordLengths(['the','cat','is','hungry']))
print(biggest([3,-1,5,-2,7,2,1]))