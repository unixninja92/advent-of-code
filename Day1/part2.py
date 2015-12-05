def part2( fname ):
    inputfile = open(fname)
    line = inputfile.readline()
    inputfile.close()
    floor = 0
    pos = 0
    for x in line:
        if x == '(':
            floor += 1
        elif x == ')':
            floor -=  1
        pos += 1
        if floor < 0:
            break
    return pos

print(part2("input"))
