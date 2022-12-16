from copy import deepcopy
import math

with open('testinput.txt') as f:
    dataSet = f.readlines()



#part 1
maxNumber = 999999999
startCoord = [maxNumber,maxNumber]
endCoord = [maxNumber,maxNumber]

grid = []
isVisted = []


for lineIndex, line in enumerate(dataSet):
    grid.append([])
    isVisted.append([])
    for charIndex, char in enumerate(line.strip('\n')):
        if char == 'S':
            startCoord = [lineIndex, charIndex]
            char = 'a'
        if char == 'E':
            endCoord = ([lineIndex, charIndex])
            char = 'z'
        grid[lineIndex].append(ord(char)-97)
        isVisted[lineIndex].append('.')

heap = []
heap.append([0,startCoord[0],startCoord[1]])

while True:
    dist, lineIndex, charIndex = heap.pop(0)

    if isVisted[lineIndex][charIndex] == '.':

        if [lineIndex,charIndex] == endCoord: 
            break

        directionPicked = False

        #check left
        if (0 < charIndex <= len(grid[0])-1):
            newLineIndex = lineIndex
            newCharIndex = charIndex - 1
            if isVisted[newLineIndex][newCharIndex] == '.':
                if (grid[newLineIndex][newCharIndex] - grid[lineIndex][charIndex]) < 2:
                    isVisted[lineIndex][charIndex] = '<'
                    heap.append([dist + 1,newLineIndex,newCharIndex])
                    directionPicked = True

        #check right
        if (0 <= charIndex < len(grid[0])-1):
            newLineIndex = lineIndex
            newCharIndex = charIndex + 1
            if isVisted[newLineIndex][newCharIndex] == '.':
                if (grid[newLineIndex][newCharIndex] - grid[lineIndex][charIndex]) < 2:
                    isVisted[lineIndex][charIndex] = '>'
                    heap.append([dist + 1,newLineIndex,newCharIndex])
                    directionPicked = True

        #check up
        if (0 < lineIndex <= len(grid)-1):
            newLineIndex = lineIndex - 1
            newCharIndex = charIndex
            if isVisted[newLineIndex][newCharIndex] == '.':
                if (grid[newLineIndex][newCharIndex] - grid[lineIndex][charIndex]) < 2:
                    isVisted[lineIndex][charIndex] = '^'
                    heap.append([dist + 1,newLineIndex,newCharIndex])
                    directionPicked = True

        #check down
        if (0 <= lineIndex < len(grid)-1):
            newLineIndex = lineIndex + 1
            newCharIndex = charIndex
            if isVisted[newLineIndex][newCharIndex] == '.':
                if (grid[newLineIndex][newCharIndex] - grid[lineIndex][charIndex]) < 2:
                    isVisted[lineIndex][charIndex] = 'v'
                    heap.append([dist + 1,newLineIndex,newCharIndex])
                    directionPicked = True


        if directionPicked == False:
            isVisted[lineIndex][charIndex] = 'o'

print(dist)


#part 2 start at end
isVisted = []
for lineIndex, line in enumerate(grid):
    isVisted.append([])
    for charIndex, char in enumerate(grid[0]):
        isVisted[lineIndex].append('.')


heap = []
heap.append([0,endCoord[0],endCoord[1]])


while True:
    dist, lineIndex, charIndex = heap.pop(0)

    if isVisted[lineIndex][charIndex] == '.':

        if grid[lineIndex][charIndex] == 0: 
            break

        directionPicked = False

        #check left
        if (0 < charIndex <= len(grid[0])-1):
            newLineIndex = lineIndex
            newCharIndex = charIndex - 1
            if isVisted[newLineIndex][newCharIndex] == '.':
                if (grid[lineIndex][charIndex] - grid[newLineIndex][newCharIndex]) < 2:
                    isVisted[lineIndex][charIndex] = '<'
                    heap.append([dist + 1,newLineIndex,newCharIndex])
                    directionPicked = True

        #check right
        if (0 <= charIndex < len(grid[0])-1):
            newLineIndex = lineIndex
            newCharIndex = charIndex + 1
            if isVisted[newLineIndex][newCharIndex] == '.':
                if (grid[lineIndex][charIndex] - grid[newLineIndex][newCharIndex]) < 2:
                    isVisted[lineIndex][charIndex] = '>'
                    heap.append([dist + 1,newLineIndex,newCharIndex])
                    directionPicked = True

        #check up
        if (0 < lineIndex <= len(grid)-1):
            newLineIndex = lineIndex - 1
            newCharIndex = charIndex
            if isVisted[newLineIndex][newCharIndex] == '.':
                if (grid[lineIndex][charIndex] - grid[newLineIndex][newCharIndex]) < 2:
                    isVisted[lineIndex][charIndex] = '^'
                    heap.append([dist + 1,newLineIndex,newCharIndex])
                    directionPicked = True

        #check down
        if (0 <= lineIndex < len(grid)-1):
            newLineIndex = lineIndex + 1
            newCharIndex = charIndex
            if isVisted[newLineIndex][newCharIndex] == '.':
                if (grid[lineIndex][charIndex] - grid[newLineIndex][newCharIndex]) < 2:
                    isVisted[lineIndex][charIndex] = 'v'
                    heap.append([dist + 1,newLineIndex,newCharIndex])
                    directionPicked = True


        if directionPicked == False:
            isVisted[lineIndex][charIndex] = 'o'

print(dist)