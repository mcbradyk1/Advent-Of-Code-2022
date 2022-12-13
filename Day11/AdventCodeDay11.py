from copy import deepcopy
import math

totalMonkeys = 0

stItems = 0
stOperationSign = 1
stOperationNumber = 2
stDivTest = 3
stPassMonkey = 4
stFailMonkey = 5
stInspectionCounts= 6

monkeyArrayDefault = [[],'','',0,0,0,0]
monkeyArray = []


def operation(item, sign, number):
    result = 0
    if number == 'old': number = item
    else: number = int(number)
    if sign == '+': result = item + number
    if sign == '*': result = item * number
    result = math.floor(result/3)
    return result




with open('input.txt') as f:
    for line in f:
        if line == '\n':
            totalMonkeys += 1
        elif line.split()[0] == 'Monkey':
            monkeyArray.append(deepcopy(monkeyArrayDefault))
        elif line.split()[0] == 'Starting':
            for x in range(len(line.split()) - 2):
                num = line.split()[2+x]
                if (num[len(num)-1]) == ',': num = num[0:len(num)-1]
                monkeyArray[totalMonkeys][stItems].append(int(num))
        elif line.split()[0] == 'Operation:':
            monkeyArray[totalMonkeys][stOperationSign] = line.split()[4]
            monkeyArray[totalMonkeys][stOperationNumber] = line.split()[5]
        elif line.split()[0] == 'Test:':
            monkeyArray[totalMonkeys][stDivTest] = int(line.split()[3])
        elif line.split()[0] == 'If':
            if line.split()[1] == 'true:': monkeyArray[totalMonkeys][stPassMonkey] = int(line.split()[5])
            elif line.split()[1] == 'false:': monkeyArray[totalMonkeys][stFailMonkey] = int(line.split()[5])

for x in range(20):
    print('Round:',x)
    for y in range(totalMonkeys):
        for z in range(len(monkeyArray[y][stItems])):
            monkeyArray[y][stInspectionCounts] += 1
            monkeyArray[y][stItems][0] = operation(monkeyArray[y][stItems][0],monkeyArray[y][stOperationSign],monkeyArray[y][stOperationNumber])
            if (monkeyArray[y][stItems][0] % monkeyArray[y][stDivTest]) == 0:
                monkeyArray[monkeyArray[y][stPassMonkey]][stItems].append(monkeyArray[y][stItems].pop(0))

            else:
                monkeyArray[monkeyArray[y][stFailMonkey]][stItems].append(monkeyArray[y][stItems].pop(0))


countList = []
for x in range(totalMonkeys):
    countList.append(monkeyArray[x][stInspectionCounts])

firstMax = max(countList)
countList.remove(firstMax)

print(firstMax * max(countList))

