grid = []

with open('input.txt') as f:
    lines = f.readlines()

for x in range(len(lines)):
    grid.append([])
    lines[x] = lines[x].replace("\n", "")
    grid[x] = [int(x) for x in lines[x]]


#grid = [[3, 0, 3, 7, 3],[2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]] #uncomment for test input
 

#part1
visibleTreeList = []

#top check
for col in range(1, len(grid[0])-1):
    tallestTreeCoord = str(0) + ',' + str(col)
    tallestTreeHeight = grid[0][col]
    visibleTreeList.append(tallestTreeCoord)
    for row in range(1, len(grid)-1):
        if grid[row][col] > tallestTreeHeight:
            tallestTreeHeight = grid[row][col]
            tallestTreeCoord = str(row) + ',' + str(col)
            visibleTreeList.append(tallestTreeCoord)

#bottom check
for col in reversed(range(1, len(grid[0])-1)):
    tallestTreeCoord = str(len(grid[0])-1) + ',' + str(col)
    tallestTreeHeight = grid[len(grid[0])-1][col]
    visibleTreeList.append(tallestTreeCoord)
    for row in reversed(range(1, len(grid)-1)):
        if grid[row][col] > tallestTreeHeight:
            tallestTreeHeight = grid[row][col]
            tallestTreeCoord = str(row) + ',' + str(col)
            visibleTreeList.append(tallestTreeCoord)

#left check
for row in range(1, len(grid)-1):
    tallestTreeCoord = str(row) + ',' + str(0)
    tallestTreeHeight = grid[row][0]
    visibleTreeList.append(tallestTreeCoord)
    for col in range(1, len(grid[0])-1):
        if grid[row][col] > tallestTreeHeight:
            tallestTreeHeight = grid[row][col]
            tallestTreeCoord = str(row) + ',' + str(col)
            visibleTreeList.append(tallestTreeCoord)

#right check
for row in reversed(range(1, len(grid)-1)):
    tallestTreeCoord = str(row) + ',' + str(len(grid)-1)
    tallestTreeHeight = grid[row][len(grid)-1]
    visibleTreeList.append(tallestTreeCoord)

    for col in reversed(range(1, len(grid[0])-1)):
        if grid[row][col] > tallestTreeHeight:
            tallestTreeHeight = grid[row][col]
            tallestTreeCoord = str(row) + ',' + str(col)
            visibleTreeList.append(tallestTreeCoord)

cleanedVisibleTreeList = [*set(visibleTreeList)] #remove duplicates


print(len(cleanedVisibleTreeList)+4) #add the 4 corners not checked

#part2

def scenicScore(a,b):
    #up
    upCount = 0
    for row in reversed(range(0,a)):
        upCount += 1
        if grid[row][b] >= grid[a][b]:
            break

    #left
    leftCount = 0
    for col in reversed(range(0,b)):
        leftCount += 1
        if grid[a][col] >= grid[a][b]:
            break

    #right
    rightCount = 0
    for col in range(b+1,len(grid[0])):
        rightCount += 1
        if grid[a][col] >= grid[a][b]:
            break

    #down
    downCount = 0
    for row in range(a+1,len(grid)):
        downCount += 1
        if grid[row][b] >= grid[a][b]:
            break

    return(upCount*leftCount*rightCount*downCount)


maxScenicScore = 0
maxScenicScoreCoord = ''
score = 0
for row in range(1, len(grid)-1):
    for col in range(1, len(grid[0])-1):
        score = scenicScore(row,col)
        if score > maxScenicScore:
            maxScenicScore = score
            maxScenicScoreCoord = str(row) + ',' + str(col)

print(maxScenicScore)

