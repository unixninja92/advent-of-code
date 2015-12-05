def notQuiteLisp( fname ):
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

def notQuiteLisp2( fname ):
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

fname = "input"
print(notQuiteLisp(fname))
print(notQuiteLisp2(fname))
