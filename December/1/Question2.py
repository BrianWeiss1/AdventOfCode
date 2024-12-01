f = open("December/1/data.txt", "r")
data = f.readline()
lst1 = []
lst2 = []
while data != "":
    print(data)
    data = data.strip('\n')
    listData = data.split("   ")
    if listData != ['']:
        lst1.append(listData[0])
        lst2.append(listData[1])
    data = f.readline()

dic = {}
# lst1 = [3, 4, 2, 1, 3, 3]
# lst2 = [4, 3, 5, 3, 9, 3]


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
    
print(simularity)