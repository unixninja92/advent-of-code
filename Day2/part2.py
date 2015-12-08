import operator
import functools

def part2( fname ):
    infile = open(fname)
    data = infile.readlines()
    infile.close()

    totalRibbon = 0
    
    for line in data:
        dem = line.split('x')
        dem = list(map(int, dem))
        totalRibbon += functools.reduce(operator.mul, dem)
        dem.sort()
        dem.pop(2)
        totalRibbon += dem[0]*2 + dem[1]*2
    return totalRibbon

print(part2("input"))
