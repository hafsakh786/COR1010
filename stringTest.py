import numpy as np

longString = "I don't know how to say this, I hope this song's on your playlist" 

print( len(longString) )

# compute the number of chracters in longString
count = 0
for ch in longString:
    count += 1
    print(ch)
print(count, len(longString))

# make a list of unique letters in longString
uniqueLetters = []
letterSet = []
for letter in longString: 
    if letter not in uniqueLetters:
        uniqueLetters.append(letter)
for letter in longString:
     if letter not in letterSet:
            letterSet.append(letter)
        #
#
print("unique letters = ", len(uniqueLetters), uniqueLetters, )
print("unique set = ", len(letterSet), letterSet)

letterList = []
for elem in letterSet:
    letterSet.append(elem)
#
letterList2 = list( letterSet )
print(letterList)
print(letterList2)