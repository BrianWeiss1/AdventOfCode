import statistics
import numpy as np
from itertools import permutations

with open("December/5/data.txt", 'r') as f:
    text = f.read()

    total_count = 0
    splitPages = []
    checkPages = []
    normalList = text.splitlines()
    for i in normalList:
        if "|" in i:
            splitPages.append(i) 
        if ',' in i:
            checkPages.append(i)
# print(normalList)
# print(splitPages)
# print(checkPages)
correct = []

for order in checkPages:
    val = order.split(',')
    listOfVals = []
    for values in range(len(val)-1):
        oneIsCorrect = False
        for page in splitPages:
            # for i in range(0, len(val)-1, 2):
            # print(page)
            if val[0+values] in page.split("|")[0]:
                listOfVals.append(page)
                if page.split("|")[1] == val[1+values]:
                    # print("good..")
                    # print(page)
                    oneIsCorrect = True
                    continue
        if oneIsCorrect:
            continue
        else:
            break
    if oneIsCorrect:
        correct.append(order)
        # print("This doesn't work")
print(correct)
medVal = 0   
total = 0
for i in range(len(correct)):
    # print(correct[i])
    trueList = correct[i].split(',')
    total+=float(trueList[int(len(trueList)/2)])
# print(total)


incorrect = []
for i in checkPages:
    if i not in correct:
        incorrect.append(i)
print(incorrect)


def solve_page_ordering(splitPages, incorrect):
    # Create a set of invalid page connections
    rules = set()
    for page in splitPages:
        key, value = page.split("|")
        rules.add((value, key))  # Invalid order is when pages are in wrong sequence
    
    correctV2 = []
    
    for order in incorrect:
        # Convert input to list of pages
        pages = order.split(',')
        
        # Reorder using the recursive method
        reordered = re_order(pages, rules)
        correctV2.append(reordered)
    
    # Calculate total of middle page numbers
    total = sum(float(reordered[len(reordered) // 2]) for reordered in correctV2)
    
    return total, correctV2

def re_order(update, rules):
    if len(update) <= 1:
        return update

    ls = []
    rs = []

    l = update[0]
    for r in update[1:]:
        invalid_order = (r, l)
        if invalid_order in rules:
            ls.append(r)
        else:
            rs.append(r)

    return re_order(ls, rules) + [l] + re_order(rs, rules)

# Usage
total, correctV2 = solve_page_ordering(splitPages, incorrect)
print(total)
for order in correctV2:
    print(order[len(order) // 2])