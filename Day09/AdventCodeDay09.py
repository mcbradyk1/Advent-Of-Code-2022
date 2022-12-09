
headCoord = [0,0]
tailCoord = [0,0]
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
                headCoord[0] += 1
            if direction == 'L':
                headCoord[0] -= 1
            if direction == 'U':
                headCoord[1] += 1
            if direction == 'D':
                headCoord[1] -= 1

            difference[0] = headCoord[0] - tailCoord[0]
            difference[1] = headCoord[1] - tailCoord[1]

            if difference[0] > 1:
                tailCoord[0] += 1
                tailCoord[1] = headCoord[1]

            if difference[0] < -1:
                tailCoord[0] -= 1
                tailCoord[1] = headCoord[1]
                
            if difference[1] > 1:
                tailCoord[1] += 1
                tailCoord[0] = headCoord[0]

            if difference[1] < -1:
                tailCoord[1] -= 1
                tailCoord[0] = headCoord[0]

            tailList.append(str(tailCoord))


cleanTailList = set(tailList)
print("Part 1 :",len(cleanTailList))

            

