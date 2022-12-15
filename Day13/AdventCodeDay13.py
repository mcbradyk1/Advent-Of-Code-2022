#keeping this here because I worked hard on it, but I discoverd the python function eval and does the same thing but better...
"""
def parse(string):
    listOfLists = []
    justAList = []
    charHolder = 'New'

    for char in string:

        #store current list, go back to previous list, and addin current list
        if charHolder != 'New' and not char.isdigit():
            justAList = listOfLists.pop()
            justAList.append(int(charHolder))
            charHolder = 'New'

        #append current working list and creat a new on
        if char == '[':
            listOfLists.append(justAList)
            justAList = []

        #store current list, go back to previous list, and addin current list
        elif char == ']':
            tempList = justAList
            justAList = listOfLists.pop()
            justAList.append(tempList)

        elif char.isdigit():
            if charHolder == 'New':
                charHolder = ''
                listOfLists.append(justAList)
                justAList = []
            charHolder = charHolder + char
    return justAList[0] #pull off the extra list
"""


with open('input.txt') as f:
    data = f.readlines()

leftArray = []
rightArray = []

x = 0
while x < len(data):
    leftArray.append(eval(data[x]))
    rightArray.append(eval(data[x+1]))
    x += 3

print('Parsing Done')



