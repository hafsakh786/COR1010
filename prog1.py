import numpy as np

arrayNumber = np.random.randint(0, 10, size=20)
print(arrayNumber)

# to make a group of unique numbers
# A = [3 1 3 4 0 6 9 6 8 5 3 0 1 0 3 1 0 9 7 2]
# unique_A = [1, 3, 4, 0, 6, 9, 7, 2, 8]

uniqueList = []
for number in arrayNumber:
    if number in uniqueList:
        pass
    else:
        uniqueList.append(number)
#
print("unique: ", uniqueList)

uniqueList2 = list() # []
for number in arrayNumber:
    if number not in uniqueList2:
        uniqueList2.append(number)
#
print("unique2: ", uniqueList2)

# uniqueList3 = [number for number in arrayNumber if number not in uniqueList3]

mylist = []
mylist2 = list()

# set, dict
uniqueSet = set()
for num in arrayNumber:
    uniqueSet.add(num)
#
print(uniqueSet)
for elem in uniqueSet:
    print(elem, end=' ')
print()