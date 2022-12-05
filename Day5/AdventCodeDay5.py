with open('input.txt') as f:
    lines = f.readlines()

f.close()

for startOfCommands in range(len(lines)):
    if (lines[startOfCommands] == '\n'):
        break

numberOfStacks = int(max(lines[startOfCommands - 1].split()))
stackArray = []
for x in range(numberOfStacks):
    stackArray.append([])
    for y in range(startOfCommands-1):
        if lines[y][(4*x)+1] != ' ':
            stackArray[x].append(lines[y][(4*x)+1])
    stackArray[x].reverse()

workArray = list(stackArray)
print(stackArray)
print(workArray)
import re
startOfCommands += 1
totalCommands = len(lines) - startOfCommands

for x in range(totalCommands):
    commandArray = [ele for ele in (re.split("[a-z]",lines[startOfCommands+x].strip())) if ele] #remove unwanted letters
    commandArray = [int(number) for number in commandArray] #convert to ints

"""   
#part1
    for y in range(commandArray[0]):
        workArray[commandArray[2]-1].append(workArray[commandArray[1]-1].pop())
"""    

#part2
    tempBuffer = []
    for y in range(commandArray[0]):
        tempBuffer.append(workArray[commandArray[1]-1].pop())

    for y in range(commandArray[0]):
        workArray[commandArray[2]-1].append(tempBuffer.pop())

for x in range(numberOfStacks):
    print(workArray[x][len(workArray[x])-1])
