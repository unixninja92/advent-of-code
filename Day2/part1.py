def part1( fname ):
    infile = open(fname)
    data = infile.readlines()
    infile.close()
    
    maxSave = 31
    savedMat = [ [ -1 for i in range(maxSave) ] for j in range(maxSave)]

    totalWrapping = 0
    
    for line in data:
        dem = line.split('x')
        dem.append(dem[0])
        dem = list(map(int, dem))
        sideArea = [ 0, 0, 0 ]
        for x in range(3):
            area = savedMat[dem[x]][dem[x+1]]
            if area < 0:
                area = 2*dem[x]*dem[x+1]
                savedMat[dem[x]][dem[x+1]] = area
                savedMat[dem[x]][dem[x+1]] = area
            sideArea[x] = area
        sideArea.append(min(sideArea)/2)
        totalWrapping += sum(sideArea)
    return totalWrapping

print(part1("input"))
    
    
