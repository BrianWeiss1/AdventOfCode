with open("December/4/data.txt", 'r') as f:
    text = f.read()

    total_count = 0
    normalList = text.splitlines()
# print(lst)
horizontalList = []

for i in range(len(normalList[0])):
    horString = ""
    for j in range(len(normalList)):
        horString = horString + normalList[j][i]
    horizontalList.append(horString)
print(horizontalList)

#Diagnal:





def fowardAndReverseCount(lst):
    count = 0
    for j in range(len(lst)):
        for i in range(len(lst[j])):
            if lst[j][i:i+4] == 'XMAS' or lst[j][i:i+4] == 'SAMX': 
                count+=1
    return count
            
print(fowardAndReverseCount(normalList))