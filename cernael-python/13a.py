def solve(lines):
    dots = set()
    folds = []
    t1 = True
    for l in lines:
        if not l:
            t1 = False
            continue
        if t1:
            x, y = l.split(',')
            dots.add((int(x),int(y)))
        else:
            r = l.split()[2].split('=')
            folds.append([r[0],int(r[1])])

    dir,line = folds[0]

    adds, removes = set(), set()
    if dir == 'x':
        for d in dots:
            if d[0] > line:
                removes.add(d)
                adds.add((line*2 - d[0], d[1]))
    elif dir == 'y':
        for d in dots:
            if d[1] > line:
                removes.add(d)
                adds.add((d[0], line*2 - d[1]))
    dots |= adds
    dots -= removes

    return len(dots)

if __name__ == '__main__':
    lines = []
    with open('13.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))
