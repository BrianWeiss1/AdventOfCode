f = open("December/2/data.txt", 'r')

data = f.readline()
lst1 = []
lst2 = []
while data != "":
    data = data.strip('\n')
    listData = data.split(" ")
    if listData != ['']:
        lst1.append(listData)
    data = f.readline()

print(lst1)
# lst1.sort()
# lst2.sort()


# Problem 1
decreasing = False
increasing = False
valid = True
count = 0
for j in range(len(lst1)):
    valid = True
    decreasing = False
    increasing = False
    continueBreak = False
    for i in range(len(lst1[j])-1):
        if decreasing and float(lst1[j][i]) < float(lst1[j][i+1]):
            valid = False
        elif increasing and float(lst1[j][i]) > float(lst1[j][i+1]):
            valid = False
        if float(lst1[j][i]) > float(lst1[j][i+1]):
            decreasing = True
        elif float(lst1[j][i]) < float(lst1[j][i+1]):
            increasing = True
        if not (abs(float(lst1[j][i])-float(lst1[j][i+1])) >= 1 and abs(float(lst1[j][i])-float(lst1[j][i+1])) <= 3):
            valid = False
            
    if valid == True:
        count+=1
    else:
        # lstTest = []
        for skip in range(len(lst1[j])):
            print(lst1[j])
            lstTest = []
        # for skip in range(len([1, 3, 2, 4, 5])):
            valid = True
            decreasing = False
            increasing = False

            continueBreak = False
            lstTest = lst1[j][0:skip] + lst1[j][skip+1:len(lst1[j])]
            for i in range(len(lstTest)-1):
                
                if decreasing and float(lstTest[i]) < float(lstTest[i+1]):
                    valid = False
                elif increasing and float(lstTest[i]) > float(lstTest[i+1]):
                    valid = False
                if float(lstTest[i]) > float(lstTest[i+1]):
                    decreasing = True
                elif float(lstTest[i]) < float(lstTest[i+1]):
                    increasing = True
                if not (abs(float(lstTest[i])-float(lstTest[i+1])) >= 1 and abs(float(lstTest[i])-float(lstTest[i+1])) <= 3):
                    valid = False
            if valid == True:
                continueBreak = True
                count+=1
                break 
            

        
        
print(count)
# Problem 2