class Smallfish_number:

    def __init__(self, list):
        self.l = list[0] if type(list[0]) == 'int' else Smallfish_number(list[0])
        self.r = list[1] if type(list[1]) == 'int' else Smallfish_number(list[1])

    def add(self, other):
        pass

    def process(self):
        # only run on the top node
        while True:
            if self.explode(1):
                continue
            if self.split():
                continue
            break

    def explode(n):
        pass

    def split():
        if isinstance(self.l, int) and self.l >= 10:
            self.l = Smallfish_number([self.l // 2, (self.l + 1) // 2])
            return True
        elif isinstance(self.l, Smallfish_number):
            if self.l.split():
                return True
        if isinstance(self.r, int) and self.r >= 10:
            self.r = Smallfish_number([self.r // 2, (self.r + 1) // 2])
            return True
        elif isinstance(self.r, Smallfish_number):
            if self.r.split():
                return True
        else:
            return False

def solve(lines):
    pass


if __name__ == '__main__':
    lines = []
    with open('18.txt') as f:
        for line in f.readlines():
            lines.append(line)
    print(solve(lines))
