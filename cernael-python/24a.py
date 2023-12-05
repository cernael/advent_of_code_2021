def solve(lines):
    pass

if __name__ == '__main__':
    lines = []
    with open('24.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))
