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

lst1.sort()
lst2.sort()
# print(lst1)
if len(lst1) == len(lst2):
    print("Same Length")
    total = 0
    for i in range(len(lst1)):
        dist = abs(float(lst1[i]) - float(lst2[i]))
        total+=dist
print(total)


f.close()