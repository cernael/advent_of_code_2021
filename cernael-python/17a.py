def solve(lines):
    (x1, x2),(y1,y2) = [[int(n) for n in p.split('=')[1].split('..')] for p in lines[0].replace(',','').split()[2:]]

    # Start with max Y velocity, which is when the first step below baseline brings
    # the position to the bottom of the target area; that step has a velocity
    # of one more than the initial upward vel - that one is subtracted here
    y_vel = max([abs(y1),abs(y2)]) - 1

    while y_vel:
        # Number of steps is y_vel climbing, one sideways, another y_vel
        # descending, and a final one down to the target area
        steps = y_vel * 2 + 2
        x_vel = 0
        while True:
            x_pos = [tri_num(x_vel), tri_num(max(0, x_vel - steps))]
            x_pos = x_pos[0] - x_pos[1]
            if x_pos < min([x1, x2]):
                x_vel += 1
            elif x_pos <= max([x1, x2]):
                return (x_vel, y_vel, tri_num(y_vel))
            else:
                break
        y_vel -= 1

def tri_num(n):
    return int(n * (n+1) / 2)

if __name__ == '__main__':
    lines = []
    with open('17.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
#    print(solve(lines))
#    print('target area: x=20..30, y=-10..-5')
    print(solve(['target area: x=20..30, y=-10..-5']))
