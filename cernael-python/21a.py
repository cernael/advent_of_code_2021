def solve(lines):
    pp = [int(l.split(': ')[1]) for l in lines]
    ps = [0, 0]
    d, c, p = 0, 0, 0

    while max(ps) < 1000:
        c += 3

        d %= 100
        d += 1
        s = d
        d %= 100
        d += 1
        s += d
        d %= 100
        d += 1
        s += d

        pp[p] += s
        pp[p] %= 10
        if pp[p] == 0:
            pp[p] = 10
        ps[p] += pp[p]
        p = 0 if p else 1

    print( 'pp:',pp,'ps:', ps,'d:',d,'c:',c,'p:',p)
    return min(ps) * c

if __name__ == '__main__':
    lines = []
    with open('21.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))
#    print(solve(['Player 1 starting position: 4','Player 2 starting position: 8']))
