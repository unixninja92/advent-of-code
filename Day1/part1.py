def part1( fname ):
    inputfile = open(fname)
    line = inputfile.readline()
    inputfile.close()
    floor = 0
    for x in line:
        if x == '(':
            floor += 1
        elif x == ')':
            floor -=  1
    return floor

print(part1("input"))
