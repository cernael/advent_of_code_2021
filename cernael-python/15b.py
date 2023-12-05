import math

def solve(lines):
    map = [[((int(d) + i + j -1) % 9)+1 for  i in range(5) for d in l] for j in range(5) for l in lines]
    costs = [[math.inf for d in l*5] for l in lines*5]
    trials = [(0,1),(1,0)]
    costs[0][0] = 0

    while trials:
#    while False:
        trial = trials.pop()
        neighs = [(trial[0]+x, trial[1]+y) for (x, y) in [(0,1),(1,0),(0,-1),(-1,0)] if 0 <= trial[0]+x < len(map) and 0 <= trial[1]+y < len(map[0])]
#        print(trial, neighs)
        oldcost = costs[trial[0]][trial[1]]
        newcost = min([ costs[ n[0] ][ n[1] ] + map[trial[0]][trial[1]] for n in neighs])

#        newcosts = [costs[n] + map[trial[0]][trial[1]] for n in neighs if n in costs.keys()]
 #       newcosts = [costs[n] + map[trial[0]][trial[1]] for n in neighs]
#        print('nc:',newcost, 'oc:',oldcost, 'tr:', trial, 'm[t]:', map[trial[0]][trial[1]])
        if newcost < oldcost:
            costs[trial[0]][trial[1]] = newcost
#            costs[trial] = newcost
            trials += neighs
#            print('tr:',trials)
#    for l in costs: print (l)
#    return [''.join([str(i) for i in l]) for l in map]
    return costs[-1][-1]
#    for l in map: print(''.join([str(i) for i in l]))

if __name__ == '__main__':
    lines = []
    with open('15.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))
#    print(solve(['1163751742','1381373672','2136511328','3694931569','7463417111','1319128137','1359912421','3125421639','1293138521','2311944581']))
