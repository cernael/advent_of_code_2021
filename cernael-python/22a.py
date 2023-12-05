def solve(lines):
    inp = [[l[0], {d[0]: list(map(int, d[2:].split('..'))) for d in l[1].split(',')}] for l in lines]

    for i in inp[:8]: print(i)

if __name__ == '__main__':
    lines = []
    with open('22.txt') as f:
        for line in f.readlines():
            lines.append(line.strip().split())
    print(solve(lines))
