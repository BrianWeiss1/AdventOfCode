f = open("December/3/data.txt", 'r')

data = f.readline()
lst1 = []
totalStr = ""
while data != "":
    data = data.strip('\n')
    totalStr = totalStr + data
    if data != ['']:
        lst1.append(data)
    data = f.readline()


#Problem 1
sum = 0
for char in range(len(totalStr)):
    if totalStr[char:char+4] == 'mul(':
        notComplete = True
        i = 0
        while notComplete:
            start = char+4
            if totalStr[char+4+i:char+5+i] == ',':
                halfway = True
            elif totalStr[char+4+i:char+5+i] == ')':
                notComplete = False
                end = char+4+i
            i+=1
        splittedVals = totalStr[start:end].split(',')
        if len(splittedVals) != 2:
            continue
        try:
            splittedVals[0] = int(splittedVals[0])
            splittedVals[1] = int(splittedVals[1])
        except:
            continue
        sum+=splittedVals[0]*splittedVals[1]
print(sum)
        
    
    
#Problem 2:
continueTheMultiplication = True
sum = 0
for char in range(len(totalStr)):
    if totalStr[char:char+7] == "don't()":
        continueTheMultiplication = False
    elif totalStr[char:char+4] == "do()":
        continueTheMultiplication = True
    if totalStr[char:char+4] == 'mul(':
        notComplete = True
        i = 0
        while notComplete:
            start = char+4
            if totalStr[char+4+i:char+5+i] == ',':
                halfway = True
            elif totalStr[char+4+i:char+5+i] == ')':
                notComplete = False
                end = char+4+i
            i+=1
        splittedVals = totalStr[start:end].split(',')
        if len(splittedVals) != 2:
            continue
        try:
            splittedVals[0] = int(splittedVals[0])
            splittedVals[1] = int(splittedVals[1])
        except:
            continue
        if continueTheMultiplication:
            sum+=splittedVals[0]*splittedVals[1]
print(sum)
        