def solve(lines):
    target = [[int(n) for n in p.split('=')[1].split('..')] for p in lines[0].replace(',','').split()[2:]]
    (x1, x2),(y1,y2) = target
# (20,30),(-10,-5)
    count = 0
# 0
    # Start with max Y velocity, which is when the first step below baseline brings
    # the position to the bottom of the target area; that step has a velocity
    # of one more than the initial upward vel - that one is subtracted here
    max_y_vel = -y1 - 1
    min_y_vel = y1
    max_x_vel = x2
    min_x_vel = 0
    while tri_num(min_x_vel) < min([x1,x2]):
        min_x_vel += 1
    #return target, (max_y_vel - min_y_vel) * (max_x_vel - min_x_vel)

    x_range = range(min_x_vel, max_x_vel + 1)
    y_range = range(min_y_vel, max_y_vel + 1)
#    for l in [['X' if est_traj(target,(x, y)) else ' ' for x in x_range] for y in y_range]: print(''.join(l))
    return sum([l.count(True) for l in [[est_traj(target, (x,y)) for x in range(min_x_vel, max_x_vel + 1)] for y in range(min_y_vel, max_y_vel + 1)] ])
#    return est_traj(target, (6,9))

def est_traj(t, s):
    x_p, y_p = 0,0
    x_v, y_v = s

#    print(t)
    while True:
        x_p += x_v
        y_p += y_v
        x_v -= 1 if x_v > 0 else 0
        y_v -= 1
#        print((x_p,y_p),(x_v,y_v))

        if min(t[0]) <= x_p <= max(t[0]) and min(t[1]) <= y_p <= max(t[1]):
#            print(s)
            return True
        elif max(t[0]) < x_p or min(t[1]) > y_p:
            return False

def tri_num(n):
    return int(n * (n+1) / 2)

if __name__ == '__main__':
    lines = []
    with open('17.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))
#    print('target area: x=20..30, y=-10..-5')
#    print(solve(['target area: x=20..30, y=-10..-5']))
