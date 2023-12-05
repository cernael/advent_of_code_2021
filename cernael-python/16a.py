class Packet:

    def __init__(self, bits):
        self.version = int(bits[:3], 2)
        self.type = int(bits[3:6], 2)
        self.data, self.tail = self.parse_value(bits[6:]) if self.type == 4 else self.parse_data(bits[6:])

    def __repr__(self):
        if self.type == 4:
            return str([self.version, self.type, self.data])
        else:
            return str([self.version, self.type, [repr(p) for p in self.data]])

    def vsum(self):
        vsum = self.version
        if self.type != 4:
            vsum += sum([p.vsum() for p in self.data])
        return vsum

    def parse_value(self, data):
        value = ''
        for i in range(0, len(data), 5):
            value += data[ i + 1 : i + 5 ]
            if data[i] == '0':
                return value, data[i + 5:]
        return '', ''

    def parse_data(self, data):
        subs = []
        if data[0] == '0':
            l = int(data[ 1:16 ], 2)
            data, res = data[ 16:16+l ], data[16+ l: ]
            while data:
                packet = Packet(data)
                data = packet.tail
                subs.append(packet)
        else:
            n = int(data[1 : 12 ], 2)
            data = data[12:]
            while n:
                n -= 1
                packet = Packet(data)
                data = packet.tail
                subs.append(packet)
            res = data
        return subs,res


def solve(line):
    bits = bin(int('1'+line,16))[3:]

    p =  Packet(bits)

    return p.vsum()

if __name__ == '__main__':
    lines = []
    with open('16.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines[0]))
