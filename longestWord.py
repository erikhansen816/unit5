#Erik Hansen
#11/13/17
#longestWord.py - finds longest word in list

words = input('Enter a list of words: ').split(' ')


l = 0
word = ""
for h in words:
    lenn = len(h)
    if lenn > l:
        l = lenn
        word = h
print("The longest word is", word)
