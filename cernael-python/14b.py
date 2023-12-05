def solve(lines):
    template = lines.pop(0)
    rules = {}
    letters = {c:0 for c in template}
    rounds = 10
    for l in lines[1:]:
        s,i = l.split(' -> ')
        letters[i] = 0
        rules[s] = [(s[0]+i, i+s[1]),0]

    for i in range(len(template)-1):
        s = template[i:i+2]
        rules[s][1] += 1

    while rounds:
        rounds -= 1
        upd = {}
        for k in rules.keys():
            upd[k] = 0
        for v in rules.values():
            upd[ v[0][0] ] += v[1]
            upd[ v[0][1] ] += v[1]
        for k,v in upd.items():
            rules[k][1] = v

    for k,v in rules.items():
        letters[k[0]] += v[1]

    letters[template[-1]] += 1
    ret = sorted(letters.values())

    return ret[-1] - ret[0]

if __name__ == '__main__':
    lines = []
    with open('14.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))

