headCoord = [[0,0],[0,0]]
direction = ''
numberOfMoves = 0
tailList = []

difference = [0,0]

with open('input.txt') as f:
    for line in f:
        direction = line.split()[0]
        numberOfMoves = int(line.split()[1])

        for x in range(numberOfMoves):
            if direction == 'R':
                headCoord[0][0] += 1
            if direction == 'L':
                headCoord[0][0] -= 1
            if direction == 'U':
                headCoord[0][1] += 1
            if direction == 'D':
                headCoord[0][1] -= 1

            difference[0] = headCoord[0][0] - headCoord[1][0]
            difference[1] = headCoord[0][1] - headCoord[1][1]

            if difference[0] > 1:
                headCoord[1][0] += 1
                headCoord[1][1] = headCoord[0][1]

            if difference[0] < -1:
                headCoord[1][0] -= 1
                headCoord[1][1] = headCoord[0][1]
                
            if difference[1] > 1:
                headCoord[1][1] += 1
                headCoord[1][0] = headCoord[0][0]

            if difference[1] < -1:
                headCoord[1][1] -= 1
                headCoord[1][0] = headCoord[0][0]

            tailList.append(str(headCoord[1]))

cleanTailList = set(tailList)
print("Part 1 :",len(cleanTailList))

            

#part 2
headCoord = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
direction = ''
numberOfMoves = 0
tailList = []

difference = [0,0]

with open('input.txt') as f:
    for line in f:
        direction = line.split()[0]
        numberOfMoves = int(line.split()[1])

        for x in range(numberOfMoves):
            if direction == 'R':
                headCoord[0][0] += 1
            if direction == 'L':
                headCoord[0][0] -= 1
            if direction == 'U':
                headCoord[0][1] += 1
            if direction == 'D':
                headCoord[0][1] -= 1

            for index in range(10):

                difference[0] = headCoord[index][0] - headCoord[index+1][0]
                difference[1] = headCoord[index][1] - headCoord[index+1][1]

                if difference[0] > 1:
                    headCoord[index+1][0] += 1
                    if difference[1] > 1:
                        pass
                    elif difference[1] < -1:
                        pass
                    else:
                        headCoord[index+1][1] = headCoord[index][1]

                if difference[0] < -1:
                    headCoord[index+1][0] -= 1
                    if difference[1] > 1:
                        pass
                    elif difference[1] < -1:
                        pass
                    else:
                        headCoord[index+1][1] = headCoord[index][1]
                    
                if difference[1] > 1:
                    headCoord[index+1][1] += 1
                    if difference[0] > 1:
                        pass
                    elif difference[0] < -1:
                        pass
                    else:
                        headCoord[index+1][0] = headCoord[index][0]

                if difference[1] < -1:
                    headCoord[index+1][1] -= 1
                    if difference[0] > 1:
                        pass
                    elif difference[0] < -1:
                        pass
                    else:
                        headCoord[index+1][0] = headCoord[index][0]

            tailList.append(str(headCoord[9]))

cleanTailList = set(tailList)
#print(tailList)
print("Part 2 :",len(cleanTailList))