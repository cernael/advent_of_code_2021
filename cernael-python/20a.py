def solve(alg, lines):
    first_step = '.'
    odd_steps = alg[int(('0' if first_step == '.' else '1')*9, 2)]

    lines = widen(lines, first_step)
    for l in lines: print(l)
    print()

    lines = widen(lines, first_step)
    lines = transform(alg, lines)

    for l in lines: print(l)
    print()

    lines = widen(lines, odd_steps)
    lines = transform(alg, lines)

    for l in lines: print(l)
    print()

    return ''.join(lines).count('#')

def transform(alg, lines):
    m = {'.':'0','#':'1'}
    h, w = len(lines), len(lines[0])

    return [''.join(
               [
                   alg[
                       int(
                           m[lines[((1+i-1) % h)-1][((1+j-1) % w)-1]] + m[lines[((1+i-1) % h)-1][((1+ j)  % w)-1]] + m[lines[((1+i-1) % h)-1][((1+j+1) % w)-1]] +
                           m[lines[((1+ i ) % h)-1][((1+j-1) % w)-1]] + m[lines[((1+ i ) % h)-1][((1+ j)  % w)-1]] + m[lines[((1+ i ) % h)-1][((1+j+1) % w)-1]] +
                           m[lines[((1+i+1) % h)-1][((1+j-1) % w)-1]] + m[lines[((1+i+1) % h)-1][((1+ j)  % w)-1]] + m[lines[((1+i+1) % h)-1][((1+j+1) % w)-1]]
                       ,2)
                   ]
                   for j in range(w)
               ]
           )
               for i in range(h)
    ]

def widen(lines, char):
    nlines = [line + char*2 for line in lines]
    lines = [char * len(nlines[0])] + [char + line + char for line in nlines] + [char * len(nlines[0])]
    return lines


if __name__ == '__main__':
    lines = []
    with open('20.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
#    print(solve(lines[0], lines[2:]))


    lines = ['..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#',
'',
'#..#.',
'#....',
'##..#',
'..#..',
'..###']
    print(solve(lines[0], lines[2:]))
