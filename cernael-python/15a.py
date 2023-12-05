import math

def solve(lines):
    map = [[int(d) for d in l] for l in lines]
    costs = [[math.inf for d in l] for l in lines]
    costs[0][0] = 0
    trials = [(0,1),(1,0)]

    while trials:
        trial = trials.pop()
        neighs = [(trial[0]+x, trial[1]+y) for (x, y) in [(0,1),(1,0),(0,-1),(-1,0)] if 0 <= trial[0]+x < len(map) and 0 <= trial[1]+y < len(map[0])]
        oldcost = costs[trial[0]][trial[1]]
        newcost = min([ costs[ n[0] ][ n[1] ] + map[trial[0]][trial[1]] for n in neighs])

        if newcost < oldcost:
            costs[trial[0]][trial[1]] = newcost
            trials += neighs

    return costs[-1][-1]

if __name__ == '__main__':
    lines = []
    with open('15.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))
