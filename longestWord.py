#Erik Hansen
#11/13/17
#longestWord.py - finds longest word in list

words = input('Enter a list of words: ').split(' ')


l = 0
word = ""
for w in words:
    length = len(w)
    if length > l:
        l = length
        word = w
print("The longest word is", word)
