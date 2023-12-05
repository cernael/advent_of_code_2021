def solve(lines):
    template = lines.pop(0)
    rules = {}
    rounds = 10
    for l in lines[1:]:
        r = l.split(' -> ')
        if r[0][0] not in rules.keys():
            rules[ r[0][0] ] = {}
        rules[ r[0][0] ][ r[0][1] ] = r[1]

    while rounds:
        rounds -= 1
        ns = template[0]
        for i in range(1, len(template)):
            ns += rules[ ns[-1] ][ template[i] ] + template[i]
        template = ns
    counts = sorted([template.count(c) for c in rules.keys()])

    return counts[-1] - counts[0]

if __name__ == '__main__':
    lines = []
    with open('14.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))
