filename = "pg84.txt"
filehandler = open(filename, "r", encoding='utf-8')


n = 0
ulist = []
while True:
    line = filehandler.readline()
    if not line:
        break
    n += 1
    for letter in line:
        if letter not in ulist:
            ulist.append(letter)

    # print(n, line)
    # if n > 3 :
    #   break
#
print(n, len(ulist), ulist)

   