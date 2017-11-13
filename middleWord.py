#Erik Hansen
#11/13/17
#middleWord.py - prints out middle word

words = input('Enter words: ').split(' ')
middle = len(words)

if middle%2 == 0:
    print(words[middle/2-1], words[middle/2])
else:
    print(words[middle//2])