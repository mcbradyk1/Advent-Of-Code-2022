directoryList = [['']]
directorySize = [['',0]]
directoryCount = 0

fullpath = '/'


with open('input.txt') as f:
    for line in f:
        if '$ cd /' in line:
            directoryList[0][0] = line.split()[2]
            fullpath = '/'

        elif '$ cd ..' in line:
            if fullpath != '/':
                index = fullpath.rfind('->')
                fullpath = fullpath[0:index]

        elif '$ cd ' in line:
            fullpath = fullpath + '->' + line.split()[2]
            directoryList.append([''])
            directorySize.append(['',0])
            directoryCount += 1
            directoryList[directoryCount][0] = fullpath

        elif '$' not in line:
            if 'dir' in line:
                directoryList[directoryCount].append(fullpath + '->' + line.split()[1])
            else:
                directoryList[directoryCount].append(line.split()[0])
            
print('Part 1')

print('Directory List')
print(directoryList)

while directoryCount > -1:
    total = 0
    for x in range(1, len(directoryList[directoryCount])):
        if directoryList[directoryCount][x].isnumeric():
            total += int(directoryList[directoryCount][x])
        else:
            for y in range(len(directorySize)):
                if directoryList[directoryCount][x] == directorySize[y][0]:
                    total += directorySize[y][1]

    directorySize[directoryCount][0] = directoryList[directoryCount][0]
    directorySize[directoryCount][1] = total
    directoryCount -= 1

print('Directory Size')
print(directorySize)

total = 0
for x in range(len(directorySize)):
    if directorySize[x][1] <= 100000:
        total += directorySize[x][1]

print('Total')
print(total)



print('Part 2')

freeSize = 70000000 - directorySize[0][1]
deleteSize = 30000000 - freeSize

currentDeleteIndex = 0

for x in range(len(directorySize)):
    if directorySize[x][1] >= deleteSize:
        if directorySize[currentDeleteIndex][1] >= directorySize[x][1]:
            currentDeleteIndex = x

print(directorySize[currentDeleteIndex])