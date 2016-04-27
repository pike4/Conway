def getNeighborCount(x, y, Matrix):
    count = 0
    if x > 0:
        if Matrix[y][x-1] == 1:
            count+=1
        if y > 0:
            if Matrix[y - 1][x - 1] == 1:
                count+=1
        if y < h - 1:
            if Matrix[y + 1][x - 1] == 1:
                count+=1
    if x < w - 1:
        if Matrix[y][x + 1] == 1:
            count+=1
        if y > 0:
            if Matrix[y - 1][x + 1] == 1:
                count+=1
        if y < h - 1:
            if Matrix[y + 1][x + 1] == 1:
                count+=1
    if y > 0:
        if Matrix[y - 1][x] == 1:
            count+=1
    if y < h - 1:
        if Matrix[y + 1][x] == 1:
            count+=1

    return count


def decideCellValue(x, y, Matrix):
    neighbors = getNeighborCount(x, y, Matrix)

    if Matrix[y][x] == 1:
        if neighbors > 3 or neighbors < 2:
            return 0
        else:
            return 1

    elif Matrix[y][x] == 0:
        if neighbors == 3:
            return 1
        else:
            return 0
        



w = 50
h = 50

decisionList = list()

Board =[[0 for x in range(0,w)] for y in range(0,h)];

Board[33][30] = 1;
Board[33][31] = 1;
Board[33][32] = 1;
Board[33][33] = 1;
Board[33][34] = 1;
Board[33][35] = 1;
Board[33][36] = 1;
Board[33][37] = 1;
Board[33][38] = 1;
Board[33][39] = 1;


for r in range (0, 20):
    outString = ""
    for x in range (0,w):
        outString += "|"
        for y in range (0,h):
            if Board[x][y] == 1:
                outString += "#"
            else:
                outString += "0"
        outString += "|"
        print(outString)
        outString = ""
    outString = ""
    for i in range(0, w):
        outString += "="
    print(outString)
    outString = ""    
    for x in range (0,w):
        for y in range (0,h):
            decisionList.insert(0, x)
            decisionList.insert(0, y)
            decisionList.insert(0, decideCellValue(x, y, Board))
            
    while len(decisionList) > 0:
        Board[decisionList.pop(0)][decisionList.pop(0)] = decisionList.pop(0)
        
    
        




    
            
    
    
            
