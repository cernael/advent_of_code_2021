class State:
    def __init__(self, pp, ps, p):
        self.pp = pp
        self.ps = ps
        self.p = p
        self.s = 0

    def next(self):
        pass

def solve(lines):
    pp = [int(l.split(': ')[1]) for l in lines]

#    states = {((p1p, p2p),(p1s,p2s),p): 0 for p1p in range(1,11) for p2p in range(1,11) for p1s in range(21) for p2s in range(21) for p in range(2)}
    states = {}

    for k,v in list(states.items())[87000:87100]: print(k,v)

if __name__ == '__main__':
    lines = []
    with open('21.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))
#    print(solve(['Player 1 starting position: 4','Player 2 starting position: 8']))
