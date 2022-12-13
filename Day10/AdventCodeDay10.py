prevX = 1
X = 1
cycleCount = 0
waitCount = 0
command = ''
singalStrengthSum = 0

checkList =[20,60,100,140,180,220]

with open('input.txt') as f:
    for line in f:
        command = line.split()[0]

        if command == 'addx':
            waitCount = 2
            X += int(line.split()[1])

        else:
            waitCount = 1

        for index in range(waitCount):
            cycleCount += 1
            if cycleCount in checkList:
                singalStrengthSum = singalStrengthSum + cycleCount*prevX

        prevX = X


print(singalStrengthSum)

prevX = 1
X = 1
cycleCount = 0
waitCount = 0
command = ''
crtString = ''
crtStringIndex = 0

with open('input.txt') as f:
    for line in f:
        command = line.split()[0]

        if command == 'addx':
            waitCount = 2
            X += int(line.split()[1])

        else:
            waitCount = 1

        for index in range(waitCount):
            cycleCount += 1

            if cycleCount == 8:
                pass

            if crtStringIndex in ([prevX,prevX+1,prevX-1]):
                crtString += '#'
            else:
                crtString += ' '
            
            crtStringIndex += 1

            if (crtStringIndex % 40 == 0):
                print(crtString)
                crtString = ''
                crtStringIndex = 0

        prevX = X
