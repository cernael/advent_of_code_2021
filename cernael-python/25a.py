def solve(lines):
    map = [list(l) for l in lines]
    c = 0
    moved = True
    while moved:
        c += 1
        map, moved = step(map)
#        if c in [58]:
 #           print('After', c, 'steps:')
  #          for l in map: print(''.join(l))
    return c

def step(map):
    map, m1 = move_east(map)
    map, m2 = move_south(map)
    moved = m1 or m2
    return map, moved

def move_east(map):
    moved = False
    for i in range(len(map)):
        skip = False
        wrap = map[i][0] == '.'
        for j in range(len(map[i]) - 1):
            if map[i][j] == '>' and map[i][j+1] == '.' and not skip:
                map[i][j] = '.'
                map[i][j+1] = '>'
                skip = True
                moved = True
            else:
                skip = False
        if wrap and map[i][-1] == '>' and not skip:
            map[i][0] = '>'
            map[i][-1] = '.'
            moved = True
    return map, moved

def move_south(map):
    moved = False
    for j in range(len(map[0])):
        skip = False
        wrap = map[0][j] == '.'
        for i in range(len(map) - 1):
            if map[i][j] == 'v' and map[i+1][j] == '.' and not skip:
                map[i][j] = '.'
                map[i+1][j] = 'v'
                skip = True
                moved = True
            else:
                skip = False
        if wrap and map[-1][j] == 'v' and not skip:
            map[0][j] = 'v'
            map[-1][j] = '.'
            moved = True
    return map, moved

if __name__ == '__main__':
    lines = []
    with open('25.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))
    '''print(solve([
'v...>>.vv>',
'.vv>>.vv..',
'>>.>v>...v',
'>>v>>.>.v.',
'v>v.vv.v..',
'>.>>..v...',
'.vv..>.>v.',
'v.v..>>v.v',
'....v..v.>']))


    m, _ = step([list(s) for s in  ['...>...','.......','......>','v.....>','......>','.......','..vvv..']])
    for l in m: print(''.join(l))
    print()
    m, _ = step(m)
    for l in m: print(''.join(l))
    print()
    m, _ = step(m)
    for l in m: print(''.join(l))
    print()
    m, _ = step(m)
    for l in m: print(''.join(l))
    print()
    m, _ = step(m)
    for l in m: print(''.join(l))'''
