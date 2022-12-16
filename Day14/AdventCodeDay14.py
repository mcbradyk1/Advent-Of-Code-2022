X = 0
Y = 1

#parse data
with open('input.txt') as f:
    data = f.readlines()

for idLine, line in enumerate(data):
    data[idLine]= data[idLine].strip('\n').split(' -> ')
    for idCoord, coord in enumerate(data[idLine]):
        data[idLine][idCoord] = data[idLine][idCoord].split(',')
        for idPoint, point in enumerate(data[idLine][idCoord]):
            data[idLine][idCoord][idPoint] = int(data[idLine][idCoord][idPoint])


# use set to track all filled coord
caveFill = set()

for idLine, line in enumerate(data):
    for index in range(1, len(data[idLine])):

        curX = data[idLine][index][X]
        preX = data[idLine][index - 1][X]

        curY = data[idLine][index][Y]
        preY = data[idLine][index - 1][Y]

        if curX == preX: # X coords are the same
            for y in range(min(curY,preY), max(curY,preY) + 1):
                caveFill.add((curX, y))

        if curY == preY: # Y coords are the same
            for x in range(min(curX,preX), max(curX,preX) + 1):
                caveFill.add((x, curY))


bottom = 0
for coord in caveFill:
    if bottom < coord[Y]: bottom = coord[Y]
    
count = 0
while True:

    didSandStop = False
    x,y = [500,0]
    while y <= bottom:

        if (x,y+1) not in caveFill:
            y += 1

        elif (x-1,y+1) not in caveFill:
            y += 1
            x -= 1

        elif (x+1,y+1) not in caveFill:
            y += 1
            x += 1

        else:
            caveFill.add((x,y))
            count += 1
            didSandStop = True
            break

    if didSandStop == False: break


print(count)





#part 2

# reset set
# use set to track all filled coord
caveFill = set()

for idLine, line in enumerate(data):
    for index in range(1, len(data[idLine])):

        curX = data[idLine][index][X]
        preX = data[idLine][index - 1][X]

        curY = data[idLine][index][Y]
        preY = data[idLine][index - 1][Y]

        if curX == preX: # X coords are the same
            for y in range(min(curY,preY), max(curY,preY) + 1):
                caveFill.add((curX, y))

        if curY == preY: # Y coords are the same
            for x in range(min(curX,preX), max(curX,preX) + 1):
                caveFill.add((x, curY))


bottom = 0
for coord in caveFill:
    if bottom < coord[Y]: bottom = coord[Y]

bottom += 1
    
count = 0
while True:

    didSandStop = False
    x,y = [500,0]
    while y <= bottom:

        if (x,y+1) not in caveFill and y != bottom:
            y += 1

        elif (x-1,y+1) not in caveFill and y != bottom:
            y += 1
            x -= 1

        elif (x+1,y+1) not in caveFill and y != bottom:
            y += 1
            x += 1

        else:
            if(x,y) in caveFill: # gotta check to make sure sand fell some amount
                break
            else:
                caveFill.add((x,y))
                count += 1
                didSandStop = True

                if count == 92:
                    pass
                break

    if didSandStop == False: break


print(count)