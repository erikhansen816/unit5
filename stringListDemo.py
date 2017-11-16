#Erik Hansen
#11/16/2017
#stringListDemo.py - print out words that start with a vowel

words = input('Enter a list of words: ').split(' ')

for word in words:
    if word[0] in 'aeiouAEIOU':
        print(word)
    



