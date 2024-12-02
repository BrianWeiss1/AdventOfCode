f = open("December/1/data.txt", "r")
data = f.readline()
lst1 = []
lst2 = []
while data != "":
    data = data.strip('\n')
    listData = data.split("   ")
    if listData != ['']:
        lst1.append(listData[0])
        lst2.append(listData[1])
    data = f.readline()

lst1.sort()
lst2.sort()

# Problem 1
if len(lst1) == len(lst2):
    total = 0
    for i in range(len(lst1)):
        dist = abs(float(lst1[i]) - float(lst2[i]))
        total+=dist
print(int(total))

# Problem 2
dic = {}
for i in range(len(lst2)):
    if dic.get(lst2[i]) == None:
        dic[lst2[i]] = 1
    else:
        dic[lst2[i]] += 1
        
simularity = 0    
for i in lst1:
    val = dic.get(i)
    if val != None:
        simularity+=float(dic.get(i))*float(i)
        
print(int(simularity))

f.close()