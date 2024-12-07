from itertools import product

with open("December/7/data2.txt", 'r') as f:
    text = f.read()

    total_count = 0
    normalList = text.splitlines()

sumLists = 0
for set in normalList:
    set = set.split(':')
    answer = set[0]
    test = set[1]
    test = test.split(" ")[1:]
    multiplicationTest = True
    permutations = list(product(["multi", "add"], repeat=len(test)-1))
    for perm in permutations:
        currentConcat = []
        fakeTest = test
        total = int(fakeTest[0])
        if int(set[0]) == 7290:
            if perm == ('add', 'multi'):
                pass

        for i in range(len(test)-1):
            if perm[i] == "multi": 
                total*=int(fakeTest[i+1])
            elif perm[i] == "add":
                total+=int(fakeTest[i+1])
            elif perm[i] == "concat":
                totalStr = ""
                totalStr = totalStr + str(total)
                totalStr = totalStr + str(fakeTest[i+1])

                total = int(totalStr)
        if len(currentConcat) != 0:
            currentConcat.append(total)
            totalStr = ""
            for concatStuff in currentConcat:
                totalStr = totalStr + str(concatStuff) 
            if int(totalStr) == int(answer):
                sumLists+=int(answer)
                break
        else:
            if total == int(answer):
                sumLists+=total
                break

print(sumLists)
                
        




#Problem 2
sumLists = 0
for set in normalList:
    set = set.split(':')
    answer = set[0]
    test = set[1]
    test = test.split(" ")[1:]
    multiplicationTest = True
    permutations = list(product(["multi", "add", 'concat'], repeat=len(test)-1))
    for perm in permutations:
        currentConcat = []
        fakeTest = test
        total = int(fakeTest[0])
        if int(set[0]) == 7290:
            if perm == ('multi', 'concat', 'multi'):
                pass

        for i in range(len(test)-1):
            if perm[i] == "multi": 
                total*=int(fakeTest[i+1])
            elif perm[i] == "add":
                total+=int(fakeTest[i+1])
            elif perm[i] == "concat":
                totalStr = ""
                totalStr = totalStr + str(total)
                totalStr = totalStr + str(fakeTest[i+1])

                total = int(totalStr)
        if len(currentConcat) != 0:
            currentConcat.append(total)
            totalStr = ""
            for concatStuff in currentConcat:
                totalStr = totalStr + str(concatStuff) 
            if int(totalStr) == int(answer):
                sumLists+=int(answer)
                break
        else:
            if total == int(answer):
                sumLists+=total
                break

print(sumLists)
                
        
